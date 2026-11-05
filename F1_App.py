from sqlalchemy import create_engine, String, Integer, Float, ForeignKey, select, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from tkinter import *
from f1_dialog import *


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = "teams"

    Team_ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Team_Name: Mapped[str] = mapped_column(String(100))


class Driver(Base):
    __tablename__ = "drivers"

    Driver_ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Driver_Name: Mapped[str] = mapped_column(String(100))
    Nationality: Mapped[str] = mapped_column(String(100))
    Driver_Number: Mapped[int] = mapped_column(Integer)
    Team_ID: Mapped[int] = mapped_column(ForeignKey("teams.Team_ID"))


class Race(Base):
    __tablename__ = "races"

    Race_ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Race_Name: Mapped[str] = mapped_column(String(100))
    Circuit: Mapped[str] = mapped_column(String(100))
    Country: Mapped[str] = mapped_column(String(100))
    Race_Date: Mapped[str] = mapped_column(String(20))
    Round: Mapped[int] = mapped_column(Integer)


class Race_Result(Base):
    __tablename__ = "race_results"

    Result_ID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Driver_ID: Mapped[int] = mapped_column(ForeignKey("drivers.Driver_ID"))
    Race_ID: Mapped[int] = mapped_column(ForeignKey("races.Race_ID"))
    Starting_Position: Mapped[int] = mapped_column(Integer)
    Finishing_Position: Mapped[int] = mapped_column(Integer)
    Points: Mapped[float] = mapped_column(Float)
    Fastest_Lap_Time: Mapped[str] = mapped_column(String(20))
    Status: Mapped[str] = mapped_column(String(50))

engine = create_engine("sqlite:///f1_database.db", echo=False)
Base.metadata.create_all(engine)



with Session(engine) as session:
    team_names = [
        "McLaren",
        "Ferrari",
        "Red Bull Racing",
        "Mercedes",
        "Aston Martin",
        "Alpine",
        "Williams",
        "Haas",
        "Racing Bulls",
        "Audi",
        "Cadillac"
    ]

    for team_name in team_names:
        statement = select(Team).where(Team.Team_Name == team_name)
        team = session.scalars(statement).first()

        if team is None:
            session.add(Team(Team_Name=team_name))

    session.commit()

    drivers = [
        ("Lando Norris", "British", 1, "McLaren"),
        ("Oscar Piastri", "Australian", 81, "McLaren"),
        ("Charles Leclerc", "Monegasque", 16, "Ferrari"),
        ("Lewis Hamilton", "British", 44, "Ferrari"),
        ("Max Verstappen", "Dutch", 3, "Red Bull Racing"),
        ("Isack Hadjar", "French", 6, "Red Bull Racing"),
        ("George Russell", "British", 63, "Mercedes"),
        ("Kimi Antonelli", "Italian", 12, "Mercedes"),
        ("Fernando Alonso", "Spanish", 14, "Aston Martin"),
        ("Lance Stroll", "Canadian", 18, "Aston Martin"),
        ("Pierre Gasly", "French", 10, "Alpine"),
        ("Franco Colapinto", "Argentine", 43, "Alpine"),
        ("Alexander Albon", "Thai", 23, "Williams"),
        ("Carlos Sainz", "Spanish", 55, "Williams"),
        ("Esteban Ocon", "French", 31, "Haas"),
        ("Oliver Bearman", "British", 87, "Haas"),
        ("Liam Lawson", "New Zealander", 30, "Racing Bulls"),
        ("Arvid Lindblad", "British", 41, "Racing Bulls"),
        ("Nico Hulkenberg", "German", 27, "Audi"),
        ("Gabriel Bortoleto", "Brazilian", 5, "Audi"),
        ("Valtteri Bottas", "Finnish", 77, "Cadillac"),
        ("Sergio Perez", "Mexican", 11, "Cadillac"),
        ("Yuki Tsunoda", "Japanese", 22, "Racing Bulls")
    ]

    for driver_name, nationality, number, team_name in drivers:
        statement = select(Driver).where(Driver.Driver_Name == driver_name)
        driver = session.scalars(statement).first()

        if driver is None:
            statement = select(Team).where(Team.Team_Name == team_name)
            team = session.scalars(statement).first()

            session.add(Driver(Driver_Name=driver_name,Nationality=nationality,Driver_Number=number,Team_ID=team.Team_ID))

    session.commit()

    races = [
        ("Australian Grand Prix", "Albert Park Grand Prix Circuit", "Australia", "2026-03-08", 1),
        ("Chinese Grand Prix", "Shanghai International Circuit", "China", "2026-03-15", 2),
        ("Japanese Grand Prix", "Suzuka International Racing Course", "Japan", "2026-03-29", 3),
        ("Miami Grand Prix", "Miami International Autodrome", "United States", "2026-05-03", 4),
        ("Canadian Grand Prix", "Circuit Gilles-Villeneuve", "Canada", "2026-05-24", 5),
        ("Monaco Grand Prix", "Circuit de Monaco", "Monaco", "2026-06-07", 6),
        ("Barcelona-Catalunya Grand Prix", "Circuit de Barcelona-Catalunya", "Spain", "2026-06-14", 7),
        ("Austrian Grand Prix", "Red Bull Ring", "Austria", "2026-06-28", 8),
        ("British Grand Prix", "Silverstone Circuit", "United Kingdom", "2026-07-05", 9),
        ("Belgian Grand Prix", "Circuit de Spa-Francorchamps", "Belgium", "2026-07-19", 10),
        ("Hungarian Grand Prix", "Hungaroring", "Hungary", "2026-07-26", 11),
        ("Dutch Grand Prix", "Circuit Zandvoort", "Netherlands", "2026-08-23", 12),
        ("Italian Grand Prix", "Autodromo Nazionale Monza", "Italy", "2026-09-06", 13),
        ("Spanish Grand Prix", "Madrid IFEMA Circuit", "Spain", "2026-09-13", 14),
        ("Azerbaijan Grand Prix", "Baku City Circuit", "Azerbaijan", "2026-09-26", 15),
        ("Bahrain Grand Prix", "Sepang International Circuit", "Malaysia", "2026-10-04", 16),
        ("Singapore Grand Prix", "Marina Bay Street Circuit", "Singapore", "2026-10-11", 17),
        ("United States Grand Prix", "Circuit of the Americas", "United States", "2026-10-25", 18),
        ("Mexico City Grand Prix", "Autodromo Hermanos Rodriguez", "Mexico", "2026-11-01", 19),
        ("Sao Paulo Grand Prix", "Interlagos", "Brazil", "2026-11-08", 20),
        ("Las Vegas Grand Prix", "Las Vegas Strip Circuit", "United States", "2026-11-21", 21),
        ("Qatar Grand Prix", "Lusail International Circuit", "Qatar", "2026-11-29", 22),
        ("Abu Dhabi Grand Prix", "Yas Marina Circuit", "United Arab Emirates", "2026-12-06", 23),
        #sprints
        ("Chinese Grand Prix Sprint", "Shanghai International Circuit", "China", "2026-03-14", 24),
        ("Miami Grand Prix Sprint", "Miami International Autodrome", "United States", "2026-05-02", 25),
        ("Canadian Grand Prix Sprint", "Circuit Gilles-Villeneuve", "Canada", "2026-05-23", 26),
        ("British Grand Prix Sprint", "Silverstone Circuit", "United Kingdom", "2026-07-04", 27),
        ("Dutch Grand Prix Sprint", "Circuit Zandvoort", "Netherlands", "2026-08-22", 28),
        ("Singapore Grand Prix Sprint", "Marina Bay Street Circuit", "Singapore", "2026-10-10", 29)
    ]

    for race_name, circuit, country, race_date, round_number in races:
        statement = select(Race).where(Race.Round == round_number)
        race = session.scalars(statement).first()

        if race is None:
            session.add(Race(Race_Name=race_name,Circuit=circuit,Country=country,Race_Date=race_date,Round=round_number))
        else:
            race.Race_Name = race_name
            race.Circuit = circuit
            race.Country = country
            race.Race_Date = race_date

    session.commit()

def insertRaceResults(raceName, raceResults):
    with Session(engine) as session:
        race = session.scalar(select(Race).where(Race.Race_Name == raceName))

        if race is not None:
            driverNumbers = [
                result[0] for result in raceResults
            ]

            validDriverIDs = session.scalars(select(Driver.Driver_ID).where(Driver.Driver_Number.in_(driverNumbers))).all()

            session.execute(
                delete(Race_Result).where(Race_Result.Race_ID == race.Race_ID,Race_Result.Driver_ID.not_in(validDriverIDs)))

            for driverNumber, starting, finishing, points, fastestLap, status in raceResults:
                driver = session.scalar(select(Driver).where(Driver.Driver_Number == driverNumber))

                if driver is not None:
                    existingResult = session.scalar(select(Race_Result).where(Race_Result.Driver_ID == driver.Driver_ID,Race_Result.Race_ID == race.Race_ID))

                    if existingResult is None:
                        existingResult = Race_Result(Driver_ID=driver.Driver_ID,Race_ID=race.Race_ID,Starting_Position=starting,Finishing_Position=finishing,Points=points,Fastest_Lap_Time=fastestLap,
                            Status=status)
                        session.add(existingResult)
                    else:
                        existingResult.Starting_Position = starting
                        existingResult.Finishing_Position = finishing
                        existingResult.Points = points
                        existingResult.Fastest_Lap_Time = fastestLap
                        existingResult.Status = status

            session.commit()



australianResults = [
    (63, 1, 1, 25, '1:22.670', 'Finished'),
    (12, 2, 2, 18, '1:22.417', 'Finished'),
    (6, 3, 0, 0, '1:25.239', 'Not Classified'),
    (16, 4, 3, 15, '1:22.579', 'Finished'),
    (81, 5, 0, 0, '', 'Did Not Start'),
    (1, 6, 5, 10, '1:22.358', 'Finished'),
    (44, 7, 4, 12, '1:22.423', 'Finished'),
    (30, 8, 13, 0, '1:23.783', 'Finished'),
    (41, 9, 8, 4, '1:24.182', 'Finished'),
    (5, 10, 9, 2, '1:23.257', 'Finished'),
    (27, 11, 0, 0, '', 'Did Not Start'),
    (87, 12, 7, 6, '1:24.020', 'Finished'),
    (31, 13, 11, 0, '1:24.424', 'Finished'),
    (10, 14, 10, 1, '1:24.486', 'Finished'),
    (23, 15, 12, 0, '1:24.375', 'Finished'),
    (43, 16, 14, 0, '1:22.926', 'Finished'),
    (14, 17, 0, 0, '1:25.713', 'Not Classified'),
    (11, 18, 16, 0, '1:26.070', 'Finished'),
    (77, 19, 0, 0, '1:27.364', 'Not Classified'),
    (3, 20, 6, 8, '1:22.091', 'Finished'),
    (55, 21, 15, 0, '1:23.590', 'Finished'),
    (18, 22, 0, 0, '1:25.410', 'Not Classified')
]

chineseSprintResults = [
    (63, 1, 1, 8, '1:35.101', 'Finished'),
    (12, 2, 5, 4, '1:34.760', 'Finished'),
    (1, 3, 4, 5, '1:35.708', 'Finished'),
    (44, 4, 3, 6, '1:34.926', 'Finished'),
    (81, 5, 6, 3, '1:35.635', 'Finished'),
    (16, 6, 2, 7, '1:34.753', 'Finished'),
    (10, 7, 11, 0, '1:38.349', 'Finished'),
    (3, 8, 9, 0, '1:35.774', 'Finished'),
    (87, 9, 8, 1, '1:37.374', 'Finished'),
    (6, 10, 15, 0, '1:36.912', 'Finished'),
    (27, 11, 0, 0, '1:38.027', 'Not Classified'),
    (31, 12, 10, 0, '1:37.363', 'Finished'),
    (30, 13, 7, 2, '1:37.882', 'Finished'),
    (5, 14, 13, 0, '1:37.800', 'Finished'),
    (41, 15, 0, 0, '1:38.475', 'Not Classified'),
    (43, 16, 14, 0, '1:37.278', 'Finished'),
    (55, 17, 12, 0, '1:37.913', 'Finished'),
    (14, 18, 17, 0, '1:38.487', 'Finished'),
    (18, 19, 18, 0, '1:38.532', 'Finished'),
    (77, 20, 0, 0, '1:39.262', 'Not Classified'),
    (11, 21, 19, 0, '1:38.862', 'Finished'),
    (23, 22, 16, 0, '1:38.158', 'Finished')
]

chineseResults = [
    (12, 1, 1, 25, '1:35.275', 'Finished'),
    (63, 2, 2, 18, '1:35.400', 'Finished'),
    (44, 3, 3, 15, '1:36.092', 'Finished'),
    (16, 4, 4, 12, '1:36.011', 'Finished'),
    (81, 5, 0, 0, '', 'Did Not Start'),
    (1, 6, 0, 0, '', 'Did Not Start'),
    (10, 7, 6, 8, '1:36.505', 'Finished'),
    (3, 8, 0, 0, '1:37.046', 'Not Classified'),
    (6, 9, 8, 4, '1:37.311', 'Finished'),
    (87, 10, 5, 10, '1:36.429', 'Finished'),
    (27, 11, 11, 0, '1:36.180', 'Finished'),
    (43, 12, 10, 1, '1:36.783', 'Finished'),
    (31, 13, 14, 0, '1:35.964', 'Finished'),
    (30, 14, 7, 6, '1:37.096', 'Finished'),
    (41, 15, 12, 0, '1:36.099', 'Finished'),
    (5, 16, 0, 0, '', 'Did Not Start'),
    (55, 17, 9, 2, '1:37.981', 'Finished'),
    (14, 18, 0, 0, '1:39.721', 'Not Classified'),
    (77, 19, 13, 0, '1:38.393', 'Finished'),
    (18, 20, 0, 0, '1:40.883', 'Not Classified'),
    (11, 21, 15, 0, '1:38.523', 'Finished'),
    (23, 22, 0, 0, '', 'Did Not Start')
]

japaneseResults = [
    (12, 1, 1, 25, '1:32.432', 'Finished'),
    (63, 2, 4, 12, '1:32.549', 'Finished'),
    (81, 3, 2, 18, '1:32.996', 'Finished'),
    (16, 4, 3, 15, '1:32.634', 'Finished'),
    (1, 5, 5, 10, '1:33.208', 'Finished'),
    (44, 6, 6, 8, '1:32.777', 'Finished'),
    (10, 7, 7, 6, '1:33.691', 'Finished'),
    (6, 8, 12, 0, '1:33.837', 'Finished'),
    (5, 9, 13, 0, '1:34.164', 'Finished'),
    (41, 10, 14, 0, '1:34.314', 'Finished'),
    (3, 11, 8, 4, '1:33.552', 'Finished'),
    (31, 12, 10, 1, '1:34.256', 'Finished'),
    (27, 13, 11, 0, '1:33.732', 'Finished'),
    (30, 14, 9, 2, '1:34.230', 'Finished'),
    (43, 15, 16, 0, '1:34.512', 'Finished'),
    (55, 16, 15, 0, '1:34.514', 'Finished'),
    (23, 17, 20, 0, '1:33.427', 'Finished'),
    (87, 18, 0, 0, '1:35.604', 'Not Classified'),
    (11, 19, 17, 0, '1:35.637', 'Finished'),
    (77, 20, 19, 0, '1:36.269', 'Finished'),
    (14, 21, 18, 0, '1:36.221', 'Finished'),
    (18, 22, 0, 0, '1:37.217', 'Not Classified')
]

miamiSprintResults = [
    (1, 1, 1, 8, '1:31.885', 'Finished'),
    (81, 2, 2, 7, '1:32.079', 'Finished'),
    (16, 3, 3, 6, '1:32.129', 'Finished'),
    (63, 4, 4, 5, '1:32.387', 'Finished'),
    (3, 5, 5, 4, '1:32.201', 'Finished'),
    (12, 6, 6, 3, '1:31.932', 'Finished'),
    (44, 7, 7, 2, '1:32.448', 'Finished'),
    (10, 8, 8, 1, '1:33.072', 'Finished'),
    (6, 9, 9, 0, '1:33.195', 'Finished'),
    (43, 10, 10, 0, '1:33.139', 'Finished'),
    (31, 11, 11, 0, '1:34.409', 'Finished'),
    (87, 12, 12, 0, '1:34.524', 'Finished'),
    (55, 13, 13, 0, '1:34.008', 'Finished'),
    (30, 14, 14, 0, '1:34.204', 'Finished'),
    (14, 15, 15, 0, '1:34.720', 'Finished'),
    (11, 16, 16, 0, '1:35.015', 'Finished'),
    (18, 17, 17, 0, '1:35.009', 'Finished'),
    (23, 18, 18, 0, '1:33.473', 'Finished'),
    (77, 19, 19, 0, '1:35.856', 'Finished'),
    (41, 21, 0, 0, '', 'Did Not Start'),
    (27, 22, 0, 0, '', 'Did Not Start'),
    (5, 20, 0, 0, '1:34.524', 'Disqualified')
]

miamiResults = [
    (12, 1, 1, 25, '1:31.968', 'Finished'),
    (3, 2, 5, 10, '1:33.110', 'Finished'),
    (16, 3, 8, 4, '1:32.515', 'Finished'),
    (1, 4, 2, 18, '1:31.869', 'Finished'),
    (63, 5, 4, 12, '1:32.446', 'Finished'),
    (44, 6, 6, 8, '1:32.676', 'Finished'),
    (81, 7, 3, 15, '1:31.949', 'Finished'),
    (43, 8, 7, 6, '1:33.035', 'Finished'),
    (10, 9, 0, 0, '1:34.856', 'Not Classified'),
    (27, 10, 0, 0, '1:34.523', 'Not Classified'),
    (30, 11, 0, 0, '1:34.814', 'Not Classified'),
    (87, 12, 11, 0, '1:33.744', 'Finished'),
    (55, 13, 9, 2, '1:33.026', 'Finished'),
    (31, 14, 13, 0, '1:33.712', 'Finished'),
    (23, 15, 10, 1, '1:33.784', 'Finished'),
    (41, 16, 14, 0, '1:34.058', 'Finished'),
    (14, 17, 15, 0, '1:34.594', 'Finished'),
    (18, 18, 17, 0, '1:34.716', 'Finished'),
    (77, 19, 18, 0, '1:36.080', 'Finished'),
    (11, 20, 16, 0, '1:34.895', 'Finished'),
    (5, 21, 12, 0, '1:33.500', 'Finished'),
    (6, 22, 0, 0, '1:34.833', 'Not Classified')
]

canadianSprintResults = [
    (63, 1, 1, 8, '1:14.702', 'Finished'),
    (1, 3, 2, 7, '1:14.596', 'Finished'),
    (12, 2, 3, 6, '1:14.380', 'Finished'),
    (81, 4, 4, 5, '1:14.793', 'Finished'),
    (16, 6, 5, 4, '1:14.741', 'Finished'),
    (44, 5, 6, 3, '1:14.695', 'Finished'),
    (3, 7, 7, 2, '1:14.974', 'Finished'),
    (41, 9, 8, 1, '1:15.653', 'Finished'),
    (43, 13, 9, 0, '1:15.478', 'Finished'),
    (55, 10, 10, 0, '1:15.943', 'Finished'),
    (30, 18, 11, 0, '1:16.257', 'Finished'),
    (5, 12, 12, 0, '1:15.980', 'Finished'),
    (31, 14, 13, 0, '1:16.849', 'Finished'),
    (11, 16, 14, 0, '1:16.641', 'Finished'),
    (27, 11, 15, 0, '1:16.297', 'Finished'),
    (18, 17, 16, 0, '1:17.120', 'Finished'),
    (77, 21, 17, 0, '1:17.212', 'Finished'),
    (87, 19, 18, 0, '1:16.210', 'Finished'),
    (23, 22, 19, 0, '1:15.717', 'Finished'),
    (10, 20, 20, 0, '1:16.150', 'Finished'),
    (6, 8, 21, 0, '1:14.941', 'Finished'),
    (14, 15, 0, 0, '1:17.543', 'Not Classified')
]

canadianResults = [
    (63, 1, 0, 0, '1:15.477', 'Not Classified'),
    (12, 2, 1, 25, '1:14.210', 'Finished'),
    (1, 3, 0, 0, '1:15.845', 'Not Classified'),
    (81, 4, 11, 0, '1:15.456', 'Finished'),
    (44, 5, 2, 18, '1:14.573', 'Finished'),
    (3, 6, 3, 15, '1:14.398', 'Finished'),
    (6, 7, 5, 10, '1:14.578', 'Finished'),
    (16, 8, 4, 12, '1:15.297', 'Finished'),
    (41, 9, 0, 0, '', 'Did Not Start'),
    (43, 10, 6, 8, '1:15.462', 'Finished'),
    (27, 11, 12, 0, '1:16.275', 'Finished'),
    (30, 12, 7, 6, '1:15.604', 'Finished'),
    (5, 13, 13, 0, '1:16.221', 'Finished'),
    (10, 14, 8, 4, '1:15.390', 'Finished'),
    (55, 15, 9, 2, '1:15.852', 'Finished'),
    (87, 16, 10, 1, '1:16.002', 'Finished'),
    (31, 17, 14, 0, '1:16.577', 'Finished'),
    (23, 18, 0, 0, '1:17.221', 'Not Classified'),
    (14, 19, 0, 0, '1:19.635', 'Not Classified'),
    (11, 20, 0, 0, '1:16.915', 'Not Classified'),
    (77, 21, 16, 0, '1:17.725', 'Finished'),
    (18, 22, 15, 0, '1:18.721', 'Finished')
]

monacoResults = [
    (12, 1, 1, 25, '1:13.481', 'Finished'),
    (3, 2, 0, 0, '', 'Not Classified'),
    (44, 3, 2, 18, '1:14.643', 'Finished'),
    (16, 4, 0, 0, '1:15.964', 'Not Classified'),
    (6, 5, 3, 15, '1:15.669', 'Finished'),
    (63, 6, 12, 0, '1:15.773', 'Finished'),
    (81, 7, 4, 12, '1:15.816', 'Finished'),
    (1, 8, 0, 0, '1:17.670', 'Not Classified'),
    (10, 9, 7, 6, '1:15.497', 'Finished'),
    (30, 10, 5, 10, '1:15.754', 'Finished'),
    (23, 11, 8, 4, '1:16.393', 'Finished'),
    (55, 12, 16, 0, '1:18.022', 'Retired'),
    (27, 13, 13, 0, '1:16.332', 'Finished'),
    (43, 14, 14, 0, '1:16.316', 'Finished'),
    (41, 15, 6, 8, '1:15.908', 'Finished'),
    (5, 16, 11, 0, '1:16.803', 'Finished'),
    (31, 17, 9, 2, '1:16.914', 'Finished'),
    (11, 18, 15, 0, '1:16.891', 'Finished'),
    (87, 19, 0, 0, '1:18.475', 'Not Classified'),
    (77, 20, 0, 0, '1:20.494', 'Not Classified'),
    (14, 21, 10, 1, '1:17.120', 'Finished'),
    (18, 22, 0, 0, '1:18.845', 'Not Classified')
]

barcelonaResults = [
    (63, 1, 2, 18, '1:20.640', 'Finished'),
    (44, 2, 1, 25, '1:20.122', 'Finished'),
    (12, 3, 0, 0, '1:20.704', 'Not Classified'),
    (1, 4, 3, 15, '1:20.232', 'Finished'),
    (3, 5, 4, 12, '1:20.230', 'Finished'),
    (6, 6, 6, 8, '1:20.150', 'Finished'),
    (81, 7, 5, 10, '1:20.835', 'Finished'),
    (30, 8, 8, 4, '1:22.691', 'Finished'),
    (27, 9, 0, 0, '1:23.447', 'Not Classified'),
    (16, 10, 0, 0, '1:20.379', 'Not Classified'),
    (41, 11, 9, 2, '1:21.914', 'Finished'),
    (5, 12, 11, 0, '1:21.446', 'Finished'),
    (43, 13, 10, 1, '1:22.449', 'Finished'),
    (10, 14, 7, 6, '1:21.960', 'Finished'),
    (87, 15, 0, 0, '1:22.419', 'Not Classified'),
    (55, 16, 12, 0, '1:22.061', 'Finished'),
    (31, 17, 13, 0, '1:21.643', 'Finished'),
    (23, 18, 0, 0, '1:21.744', 'Not Classified'),
    (11, 19, 14, 0, '1:22.820', 'Finished'),
    (77, 20, 0, 0, '1:25.745', 'Not Classified'),
    (18, 21, 0, 0, '1:25.904', 'Not Classified'),
    (14, 22, 0, 0, '1:25.366', 'Not Classified')
]

austrianResults = [
    (63, 1, 1, 25, '1:10.683', 'Finished'),
    (16, 2, 8, 4, '1:10.606', 'Finished'),
    (44, 3, 5, 10, '1:10.946', 'Finished'),
    (12, 4, 3, 15, '1:10.374', 'Finished'),
    (3, 5, 2, 18, '1:10.483', 'Finished'),
    (1, 6, 7, 6, '1:10.652', 'Finished'),
    (81, 7, 4, 12, '1:10.595', 'Finished'),
    (6, 8, 6, 8, '1:10.947', 'Finished'),
    (30, 9, 9, 2, '1:11.547', 'Finished'),
    (41, 10, 10, 1, '1:11.587', 'Finished'),
    (10, 11, 13, 0, '1:11.466', 'Finished'),
    (5, 12, 11, 0, '1:11.866', 'Finished'),
    (87, 13, 14, 0, '1:12.207', 'Finished'),
    (27, 14, 12, 0, '1:11.634', 'Finished'),
    (31, 15, 16, 0, '1:12.979', 'Finished'),
    (43, 16, 15, 0, '1:11.795', 'Finished'),
    (55, 17, 0, 0, '1:13.694', 'Not Classified'),
    (23, 18, 17, 0, '1:13.137', 'Finished'),
    (11, 19, 0, 0, '1:14.448', 'Not Classified'),
    (77, 20, 0, 0, '', 'Not Classified'),
    (14, 21, 18, 0, '1:12.501', 'Finished'),
    (18, 22, 0, 0, '1:13.796', 'Not Classified')
]

britishSprintResults = [
    (44, 1, 2, 7, '1:31.908', 'Finished'),
    (12, 2, 1, 8, '1:31.607', 'Finished'),
    (3, 3, 6, 3, '1:32.393', 'Finished'),
    (16, 4, 5, 4, '1:32.158', 'Finished'),
    (63, 5, 4, 5, '1:31.977', 'Finished'),
    (1, 6, 3, 6, '1:32.190', 'Finished'),
    (81, 7, 7, 2, '1:32.223', 'Finished'),
    (6, 8, 9, 0, '1:33.000', 'Finished'),
    (30, 9, 8, 1, '1:33.051', 'Finished'),
    (41, 10, 10, 0, '1:33.572', 'Finished'),
    (10, 11, 11, 0, '1:33.880', 'Finished'),
    (5, 12, 14, 0, '1:33.506', 'Finished'),
    (43, 13, 12, 0, '1:33.520', 'Finished'),
    (27, 14, 13, 0, '1:33.497', 'Finished'),
    (87, 15, 15, 0, '1:33.574', 'Finished'),
    (31, 16, 16, 0, '1:34.399', 'Finished'),
    (55, 17, 17, 0, '1:34.186', 'Finished'),
    (23, 18, 18, 0, '1:33.989', 'Finished'),
    (77, 19, 19, 0, '1:35.371', 'Finished'),
    (14, 20, 20, 0, '1:36.301', 'Finished'),
    (18, 21, 21, 0, '1:35.028', 'Finished'),
    (11, 22, 22, 0, '1:34.528', 'Finished')
]

britishResults = [
    (12, 1, 15, 0, '1:31.777', 'Finished'),
    (16, 2, 1, 25, '1:32.871', 'Finished'),
    (44, 3, 3, 15, '1:32.309', 'Finished'),
    (63, 4, 2, 18, '1:32.489', 'Finished'),
    (6, 5, 5, 10, '1:32.268', 'Finished'),
    (1, 6, 4, 12, '1:32.625', 'Finished'),
    (3, 7, 0, 0, '1:32.101', 'Not Classified'),
    (81, 8, 11, 0, '1:32.917', 'Finished'),
    (41, 9, 7, 6, '1:33.632', 'Finished'),
    (30, 10, 6, 8, '1:33.648', 'Finished'),
    (5, 11, 8, 4, '1:33.650', 'Finished'),
    (27, 12, 0, 0, '1:33.433', 'Not Classified'),
    (87, 13, 12, 0, '1:34.455', 'Finished'),
    (55, 14, 17, 0, '1:32.734', 'Finished'),
    (10, 15, 10, 1, '1:34.179', 'Finished'),
    (23, 16, 0, 0, '1:33.867', 'Not Classified'),
    (31, 17, 13, 0, '1:34.792', 'Finished'),
    (77, 18, 16, 0, '1:35.893', 'Finished'),
    (43, 19, 9, 2, '1:34.281', 'Finished'),
    (11, 20, 14, 0, '1:35.520', 'Finished'),
    (14, 21, 18, 0, '1:35.827', 'Finished'),
    (18, 22, 19, 0, '1:37.232', 'Finished')
]

belgianResults = [
    (12, 1, 1, 25, '1:49.098', 'Finished'),
    (3, 2, 3, 15, '1:49.618', 'Finished'),
    (63, 3, 0, 0, '', 'Not Classified'),
    (16, 4, 2, 18, '1:49.333', 'Finished'),
    (44, 5, 4, 12, '1:49.454', 'Finished'),
    (81, 6, 5, 10, '1:49.562', 'Finished'),
    (41, 7, 9, 2, '1:50.536', 'Finished'),
    (5, 8, 8, 4, '1:50.334', 'Finished'),
    (30, 9, 12, 0, '1:51.075', 'Finished'),
    (10, 10, 11, 0, '1:51.101', 'Finished'),
    (43, 11, 10, 1, '1:51.162', 'Finished'),
    (27, 12, 13, 0, '1:50.503', 'Finished'),
    (1, 13, 7, 6, '1:48.890', 'Finished'),
    (87, 14, 14, 0, '1:51.109', 'Finished'),
    (23, 15, 15, 0, '1:51.894', 'Finished'),
    (31, 16, 17, 0, '1:51.900', 'Finished'),
    (77, 17, 18, 0, '1:52.011', 'Finished'),
    (11, 18, 0, 0, '1:53.520', 'Not Classified'),
    (55, 19, 16, 0, '1:51.363', 'Finished'),
    (18, 20, 0, 0, '1:53.980', 'Not Classified'),
    (6, 21, 6, 8, '1:49.298', 'Finished'),
    (14, 22, 19, 0, '1:52.948', 'Finished')
]

hungarianResults = [
    (1, 1, 1, 25, '1:22.491', 'Finished'),
    (16, 2, 4, 12, '1:22.000', 'Finished'),
    (81, 3, 0, 0, '1:23.896', 'Not Classified'),
    (3, 4, 2, 18, '1:23.433', 'Finished'),
    (44, 5, 5, 10, '1:22.300', 'Finished'),
    (63, 6, 7, 6, '1:22.589', 'Finished'),
    (12, 7, 3, 15, '1:22.415', 'Finished'),
    (6, 8, 6, 8, '1:23.218', 'Finished'),
    (41, 9, 10, 1, '1:25.931', 'Finished'),
    (27, 10, 9, 2, '1:23.964', 'Finished'),
    (30, 11, 8, 4, '1:23.900', 'Finished'),
    (10, 12, 11, 0, '1:22.871', 'Finished'),
    (43, 13, 15, 0, '1:24.624', 'Finished'),
    (5, 14, 12, 0, '1:24.783', 'Finished'),
    (31, 15, 16, 0, '1:25.889', 'Finished'),
    (14, 16, 14, 0, '1:23.679', 'Finished'),
    (87, 17, 19, 0, '1:25.884', 'Finished'),
    (55, 18, 18, 0, '1:24.864', 'Finished'),
    (23, 19, 17, 0, '1:25.403', 'Finished'),
    (18, 20, 13, 0, '1:24.718', 'Finished'),
    (77, 21, 0, 0, '1:27.959', 'Not Classified'),
    (11, 22, 0, 0, '1:26.342', 'Not Classified')
]

dutchSprintResults = [
    (63, 1, 1, 8, '1:14.936', 'Finished'),
    (16, 3, 2, 7, '1:15.049', 'Finished'),
    (1, 2, 3, 6, '1:14.881', 'Finished'),
    (12, 5, 4, 5, '1:14.990', 'Finished'),
    (81, 4, 5, 4, '1:15.324', 'Finished'),
    (3, 6, 6, 3, '1:15.443', 'Finished'),
    (44, 7, 7, 2, '1:15.557', 'Finished'),
    (10, 8, 8, 1, '1:16.895', 'Finished'),
    (5, 9, 9, 0, '1:16.922', 'Finished'),
    (41, 10, 10, 0, '1:16.886', 'Finished'),
    (30, 11, 11, 0, '1:16.909', 'Finished'),
    (43, 13, 12, 0, '1:16.718', 'Finished'),
    (31, 15, 14, 0, '1:17.138', 'Finished'),
    (87, 17, 15, 0, '1:17.137', 'Finished'),
    (23, 16, 16, 0, '1:17.673', 'Finished'),
    (18, 18, 17, 0, '1:17.713', 'Finished'),
    (14, 22, 18, 0, '1:17.449', 'Finished'),
    (77, 19, 19, 0, '1:17.710', 'Finished'),
    (55, 21, 20, 0, '1:17.431', 'Finished'),
    (11, 20, 21, 0, '1:17.462', 'Finished'),
    (27, 14, 0, 0, '1:17.706', 'Not Classified'),
    (22, 12, 13, 0, '', 'Finished')
]

dutchResults = [
    (1, 1, 1, 25, '1:14.321', 'Finished'),
    (63, 2, 3, 15, '1:15.393', 'Finished'),
    (12, 3, 2, 18, '1:14.571', 'Finished'),
    (81, 4, 6, 8, '1:14.303', 'Finished'),
    (44, 5, 4, 12, '1:14.566', 'Finished'),
    (16, 6, 5, 10, '1:14.230', 'Finished'),
    (3, 7, 0, 0, '', 'Not Classified'),
    (30, 8, 7, 6, '1:15.435', 'Finished'),
    (5, 9, 13, 0, '1:15.515', 'Finished'),
    (41, 10, 12, 0, '1:16.653', 'Finished'),
    (10, 11, 10, 1, '1:16.220', 'Finished'),
    (27, 13, 8, 4, '1:16.048', 'Finished'),
    (43, 14, 14, 0, '1:15.578', 'Finished'),
    (31, 15, 0, 0, '1:17.588', 'Not Classified'),
    (23, 16, 17, 0, '1:17.147', 'Finished'),
    (55, 17, 16, 0, '1:17.328', 'Finished'),
    (14, 18, 9, 2, '1:16.946', 'Finished'),
    (18, 19, 0, 0, '1:17.883', 'Not Classified'),
    (87, 20, 0, 0, '', 'Not Classified'),
    (77, 21, 0, 0, '1:17.822', 'Not Classified'),
    (11, 22, 15, 0, '1:17.523', 'Finished'),
    (22, 12, 11, 0, '1:16.639', 'Finished')
]

italianResults = [
    (10, 1, 7, 6, '1:24.927', 'Finished'),
    (63, 2, 2, 18, '1:24.390', 'Finished'),
    (16, 3, 0, 0, '', 'Not Classified'),
    (44, 4, 6, 8, '1:25.300', 'Finished'),
    (3, 5, 3, 15, '1:24.242', 'Finished'),
    (81, 6, 5, 10, '1:25.125', 'Finished'),
    (43, 7, 9, 2, '1:24.933', 'Finished'),
    (1, 8, 4, 12, '1:24.864', 'Finished'),
    (41, 9, 8, 4, '1:26.028', 'Finished'),
    (5, 10, 11, 0, '1:26.188', 'Finished'),
    (12, 19, 1, 25, '1:23.504', 'Finished'),
    (27, 12, 12, 0, '1:24.364', 'Finished'),
    (30, 22, 14, 0, '1:25.578', 'Finished'),
    (55, 13, 13, 0, '1:25.683', 'Finished'),
    (87, 11, 15, 0, '1:26.356', 'Finished'),
    (31, 14, 16, 0, '1:25.711', 'Finished'),
    (23, 20, 17, 0, '1:25.341', 'Finished'),
    (11, 17, 18, 0, '1:26.914', 'Finished'),
    (77, 16, 19, 0, '1:27.325', 'Finished'),
    (14, 21, 0, 0, '1:27.961', 'Not Classified'),
    (18, 18, 0, 0, '1:28.415', 'Not Classified'),
    (22, 15, 10, 1, '1:26.320', 'Finished')
]

spanishResults = [
    (1, 1, 3, 15, '1:36.680', 'Finished'),
    (12, 2, 1, 25, '1:36.030', 'Finished'),
    (3, 3, 2, 18, '1:36.760', 'Finished'),
    (44, 4, 0, 0, '1:39.839', 'Not Classified'),
    (16, 5, 4, 12, '1:36.063', 'Finished'),
    (63, 6, 5, 10, '1:35.587', 'Finished'),
    (81, 7, 8, 4, '1:37.226', 'Finished'),
    (30, 8, 6, 8, '1:36.846', 'Finished'),
    (43, 9, 7, 6, '1:37.321', 'Finished'),
    (41, 10, 9, 2, '1:38.211', 'Finished'),
    (27, 11, 10, 1, '1:38.114', 'Finished'),
    (31, 13, 11, 0, '1:38.119', 'Finished'),
    (10, 14, 12, 0, '1:38.141', 'Finished'),
    (5, 12, 13, 0, '1:37.837', 'Finished'),
    (23, 16, 15, 0, '1:39.397', 'Finished'),
    (87, 22, 16, 0, '1:37.308', 'Finished'),
    (14, 17, 17, 0, '1:39.003', 'Finished'),
    (77, 19, 18, 0, '1:39.130', 'Finished'),
    (55, 20, 0, 0, '1:40.195', 'Not Classified'),
    (11, 18, 0, 0, '1:41.116', 'Not Classified'),
    (18, 21, 0, 0, '1:43.462', 'Not Classified'),
    (22, 15, 14, 0, '1:38.396', 'Finished')
]

azerbaijanResults = [
    (63, 1, 1, 25, '1:44.916', 'Finished'),
    (16, 2, 4, 12, '1:45.784', 'Finished'),
    (81, 3, 13, 0, '1:46.602', 'Finished'),
    (6, 4, 3, 15, '1:45.618', 'Finished'),
    (1, 5, 0, 0, '1:47.761', 'Not Classified'),
    (44, 6, 6, 8, '1:46.170', 'Finished'),
    (10, 7, 0, 0, '1:47.822', 'Not Classified'),
    (3, 8, 2, 18, '1:44.993', 'Finished'),
    (43, 9, 0, 0, '1:48.484', 'Not Classified'),
    (87, 10, 9, 2, '1:46.978', 'Finished'),
    (30, 11, 12, 0, '1:46.906', 'Finished'),
    (23, 12, 0, 0, '1:48.443', 'Not Classified'),
    (31, 13, 8, 4, '1:47.068', 'Finished'),
    (55, 14, 10, 1, '1:46.737', 'Finished'),
    (41, 15, 7, 6, '1:46.849', 'Finished'),
    (12, 16, 5, 10, '1:45.413', 'Finished'),
    (5, 17, 15, 0, '1:46.336', 'Finished'),
    (27, 18, 11, 0, '1:46.850', 'Finished'),
    (77, 19, 16, 0, '1:48.852', 'Retired'),
    (11, 20, 14, 0, '1:47.363', 'Finished'),
    (14, 21, 0, 0, '1:50.968', 'Not Classified'),
    (18, 22, 0, 0, '1:51.723', 'Not Classified')
]

bahrainResults = [
    (3, 1, 1, 25, '1:38.220', 'Finished'),
    (44, 2, 3, 15, '1:38.610', 'Finished'),
    (12, 3, 2, 18, '1:38.589', 'Finished'),
    (16, 4, 4, 12, '1:39.336', 'Finished'),
    (1, 5, 9, 2, '1:39.970', 'Finished'),
    (81, 6, 6, 8, '1:39.485', 'Finished'),
    (63, 7, 20, 0, '1:40.715', 'Retired'),
    (6, 8, 5, 10, '1:39.792', 'Finished'),
    (10, 9, 16, 0, '1:41.514', 'Finished'),
    (5, 10, 18, 0, '1:41.382', 'Finished'),
    (30, 11, 7, 6, '1:40.254', 'Finished'),
    (14, 12, 8, 4, '1:40.353', 'Finished'),
    (55, 13, 17, 0, '1:41.738', 'Finished'),
    (18, 14, 12, 0, '1:41.248', 'Finished'),
    (27, 15, 11, 0, '1:41.394', 'Finished'),
    (87, 16, 14, 0, '1:40.366', 'Finished'),
    (31, 17, 15, 0, '1:42.062', 'Finished'),
    (23, 18, 0, 0, '1:42.284', 'Not Classified'),
    (77, 19, 0, 0, '1:59.953', 'Not Classified'),
    (11, 20, 19, 0, '1:42.688', 'Finished'),
    (43, 21, 13, 0, '1:40.988', 'Finished'),
    (41, 22, 10, 1, '1:40.315', 'Finished')
]

singaporeSprintResults = [
    (3, 1, 1, 8, '1:46.017', 'Finished'),
    (44, 6, 2, 7, '1:45.457', 'Finished'),
    (16, 3, 3, 6, '1:46.738', 'Finished'),
    (12, 7, 4, 5, '1:46.862', 'Finished'),
    (30, 8, 5, 4, '1:46.272', 'Finished'),
    (87, 13, 6, 3, '1:46.966', 'Finished'),
    (27, 12, 7, 2, '1:47.310', 'Finished'),
    (1, 5, 8, 1, '1:46.892', 'Finished'),
    (10, 10, 9, 0, '1:47.776', 'Finished'),
    (31, 16, 10, 0, '1:48.012', 'Finished'),
    (14, 15, 11, 0, '1:48.596', 'Finished'),
    (55, 22, 12, 0, '1:48.643', 'Finished'),
    (41, 17, 13, 0, '1:48.684', 'Finished'),
    (81, 4, 14, 0, '1:47.088', 'Did Not Finish'),
    (23, 19, 0, 0, '1:50.860', 'Not Classified'),
    (5, 14, 0, 0, '', 'Not Classified'),
    (77, 21, 0, 0, '', 'Not Classified'),
    (6, 9, 0, 0, '', 'Not Classified'),
    (43, 11, 0, 0, '', 'Not Classified'),
    (63, 2, 0, 0, '1:50.872', 'Not Classified'),
    (11, 20, 0, 0, '', 'Not Classified'),
    (18, 18, 0, 0, '', 'Not Classified')
]

singaporeResults = [
    (3, 1, 1, 25, '1:36.201', 'Finished'),
    (16, 2, 2, 18, '1:35.202', 'Finished'),
    (44, 3, 6, 8, '1:36.922', 'Finished'),
    (12, 4, 3, 15, '1:35.589', 'Finished'),
    (1, 5, 4, 12, '1:36.282', 'Finished'),
    (81, 6, 5, 10, '1:35.665', 'Finished'),
    (10, 7, 11, 0, '1:37.390', 'Finished'),
    (30, 8, 7, 6, '1:37.193', 'Finished'),
    (41, 9, 15, 0, '1:38.154', 'Finished'),
    (27, 10, 8, 4, '1:37.055', 'Finished'),
    (87, 11, 12, 0, '1:37.556', 'Finished'),
    (31, 12, 13, 0, '1:38.129', 'Finished'),
    (55, 13, 14, 0, '1:38.326', 'Finished'),
    (5, 14, 0, 0, '1:40.486', 'Not Classified'),
    (43, 15, 0, 0, '1:39.265', 'Not Classified'),
    (23, 16, 18, 0, '1:37.436', 'Finished'),
    (11, 17, 17, 0, '1:38.574', 'Finished'),
    (77, 18, 19, 0, '1:40.171', 'Finished'),
    (63, 19, 9, 2, '1:36.722', 'Finished'),
    (14, 20, 16, 0, '1:38.032', 'Finished'),
    (18, 21, 0, 0, '1:39.137', 'Not Classified'),
    (6, 22, 10, 1, '1:35.917', 'Finished')
]

insertRaceResults("Australian Grand Prix", australianResults)
insertRaceResults("Chinese Grand Prix Sprint", chineseSprintResults)
insertRaceResults("Chinese Grand Prix", chineseResults)
insertRaceResults("Japanese Grand Prix", japaneseResults)
insertRaceResults("Miami Grand Prix Sprint", miamiSprintResults)
insertRaceResults("Miami Grand Prix", miamiResults)
insertRaceResults("Canadian Grand Prix Sprint", canadianSprintResults)
insertRaceResults("Canadian Grand Prix", canadianResults)
insertRaceResults("Monaco Grand Prix", monacoResults)
insertRaceResults("Barcelona-Catalunya Grand Prix", barcelonaResults)
insertRaceResults("Austrian Grand Prix", austrianResults)
insertRaceResults("British Grand Prix Sprint", britishSprintResults)
insertRaceResults("British Grand Prix", britishResults)
insertRaceResults("Belgian Grand Prix", belgianResults)
insertRaceResults("Hungarian Grand Prix", hungarianResults)
insertRaceResults("Dutch Grand Prix Sprint", dutchSprintResults)
insertRaceResults("Dutch Grand Prix", dutchResults)
insertRaceResults("Italian Grand Prix", italianResults)
insertRaceResults("Spanish Grand Prix", spanishResults)
insertRaceResults("Azerbaijan Grand Prix", azerbaijanResults)
insertRaceResults("Bahrain Grand Prix", bahrainResults)
insertRaceResults("Singapore Grand Prix Sprint", singaporeSprintResults)
insertRaceResults("Singapore Grand Prix", singaporeResults)


def displayTeams():
    with Session(engine) as session:
        statement = select(Team)
        teamList = session.scalars(statement).all()

    displayDialog(window, teamList, "Teams")

def displayDrivers():
    with Session(engine) as session:
        statement = select(Driver, Team).join(Team, Driver.Team_ID == Team.Team_ID).order_by(Team.Team_ID, Driver.Driver_Number)

        records = session.execute(statement).all()
        driverList = []

        for driver, team in records:
            driverList.append((driver.Driver_Number,driver.Driver_Name,driver.Nationality,team.Team_Name))

    displayDialog(window, driverList, "Drivers")

def displayRaces():
    with Session(engine) as session:
        statement = select(Race)
        raceList = session.scalars(statement).all()

    displayDialog(window, raceList, "Races")

def raceManagement():
    window2 = Toplevel(window)
    window2.geometry("400x250")
    window2.title("Race Management")

    label1 = Label(window2, text="Select Race")
    label1.place(x=30, y=40)

    with Session(engine) as session:
        statement = select(Race).order_by(Race.Round)
        raceList = session.scalars(statement).all()

        availableRaces = []

        for race in raceList:
            statement = select(Race_Result).where(Race_Result.Race_ID == race.Race_ID)
            results = session.scalars(statement).first()

            if results is None:
                availableRaces.append(race)

        raceNames = [race.Race_Name for race in availableRaces]

    raceVar = StringVar()
    raceTypeVar = StringVar()

    def updateRaceType(*args):
        if "Sprint" in raceVar.get():
            raceTypeVar.set("Sprint")
        else:
            raceTypeVar.set("Grand Prix")

    if len(raceNames) > 0:
        raceVar.set(raceNames[0])
        updateRaceType()
    else:
        raceVar.set("No races available")
        raceTypeVar.set("Grand Prix")

    raceMenu = OptionMenu(window2,raceVar,*raceNames,command=updateRaceType)
    raceMenu.config(width=25)
    raceMenu.place(x=130, y=35)

    label2 = Label(window2, text="Race Type")
    label2.place(x=30, y=100)

    raceTypeMenu = OptionMenu(window2,raceTypeVar,"Grand Prix","Sprint")
    raceTypeMenu.config(width=25)
    raceTypeMenu.place(x=130, y=95)
    raceTypeMenu.config(state="disabled")

    button1 = Button(window2,text="Continue",width=12,command=lambda: openRaceResults(raceVar.get(),raceTypeVar.get()))
    button1.place(x=75, y=170)

    button2 = Button(window2,text="Cancel",width=12,command=window2.destroy)
    button2.place(x=220, y=170)

def openRaceResults(raceName, raceType):
    window3 = Toplevel(window)
    window3.geometry("850x800")
    window3.title(raceName + " Results")

    label1 = Label(window3, text=raceName + " - Enter Race Results",font=("arial", 14, "bold"))
    label1.place(x=250, y=10)

    Label(window3, text="Driver").place(x=30, y=60)
    Label(window3, text="Finishing Position").place(x=230, y=60)
    Label(window3, text="Fastest Lap Time").place(x=360, y=60)
    Label(window3, text="Status").place(x=560, y=60)

    with Session(engine) as session:
        statement = select(Driver).order_by(Driver.Driver_Number)
        driverList = session.scalars(statement).all()

    positionEntries = []
    fastestLapEntries = []
    statusEntries = []

    y = 95

    for driver in driverList:
        driverLabel = Label(window3, text=driver.Driver_Name,width=20, anchor="w")
        driverLabel.place(x=30, y=y)

        positionEntry = Entry(window3, width=10)
        positionEntry.place(x=250, y=y)
        positionEntries.append((driver.Driver_ID, positionEntry))

        fastestLapEntry = Entry(window3, width=15)
        fastestLapEntry.place(x=370, y=y)
        fastestLapEntries.append((driver.Driver_ID, fastestLapEntry))

        status = StringVar(value="Finished")
        statusMenu = OptionMenu(window3, status, "Finished", "Retired","Not Classified", "Did Not Start", "Disqualified")
        statusMenu.config(width=15)
        statusMenu.place(x=550, y=y)
        statusEntries.append((driver.Driver_ID, status))

        y += 25

    button1 = Button(window3, text="Save Results", width=15,command=lambda: saveRaceResults(raceName, raceType, positionEntries,fastestLapEntries, statusEntries, window3))
    button1.place(x=280, y=y + 15)
    button2 = Button(window3, text="Cancel", width=15,command=window3.destroy)
    button2.place(x=450, y=y + 15)


def saveRaceResults(raceName, raceType, positionEntries,fastestLapEntries, statusEntries, window3):
    grandPrixPoints = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    sprintPoints = [8, 7, 6, 5, 4, 3, 2, 1]

    positions = []

    for driverID, positionEntry in positionEntries:
        status = ""

        for statusDriverID, statusVariable in statusEntries:
            if statusDriverID == driverID:
                status = statusVariable.get()
                break

        position = positionEntry.get().strip()

        if status == "Finished":
            if position == "" or not position.isdigit():
                return

            position = int(position)

            if position < 1 or position > len(positionEntries):
                return

            if position in positions:
                return

            positions.append(position)

    with Session(engine) as session:
        race = session.scalar(select(Race).where(Race.Race_Name == raceName))

        if race is None:
            return

        existingResult = session.scalars(
            select(Race_Result).where(Race_Result.Race_ID == race.Race_ID)).first()

        if existingResult is not None:
            return

        for driverID, positionEntry in positionEntries:
            status = ""

            for statusDriverID, statusVariable in statusEntries:
                if statusDriverID == driverID:
                    status = statusVariable.get()
                    break

            position = positionEntry.get().strip()

            if status != "Finished":
                position = 0
            else:
                position = int(position)

            fastestLap = ""

            for lapDriverID, lapEntry in fastestLapEntries:
                if lapDriverID == driverID:
                    fastestLap = lapEntry.get().strip()
                    break

            points = 0

            if status == "Finished":
                if raceType == "Sprint":
                    if position <= len(sprintPoints):
                        points = sprintPoints[position - 1]
                else:
                    if position <= len(grandPrixPoints):
                        points = grandPrixPoints[position - 1]

            result = Race_Result(Driver_ID=driverID,Race_ID=race.Race_ID,Starting_Position=position,Finishing_Position=position,Points=points,Fastest_Lap_Time=fastestLap,Status=status)
            session.add(result)

        session.commit()

    loadDriver()
    window3.destroy()


def displayResults():
    with Session(engine) as session:
        statement = select(Race).order_by(Race.Round)
        raceList = session.scalars(statement).all()

    displayRaceList(window, raceList, viewRaceResults)

def viewRaceResults(race_id, race_name):
    with (Session(engine) as session):
        statement = select(Race_Result, Driver).join(Driver, Race_Result.Driver_ID == Driver.Driver_ID).where(Race_Result.Race_ID == race_id
        ).order_by(Race_Result.Finishing_Position == 0,Race_Result.Finishing_Position)

        records = session.execute(statement).all()

        resultList = []

        for result, driver in records:
            resultList.append((driver.Driver_Name,result.Finishing_Position,result.Points,result.Fastest_Lap_Time,result.Status))

    displayRaceResultDialog(window, race_name, resultList)

currentDriverIndex = 0

def loadDriver():
    with Session(engine) as session:
        statement = select(Driver, Team).join(Team, Driver.Team_ID == Team.Team_ID).order_by(Team.Team_ID, Driver.Driver_Number)
        records = session.execute(statement).all()

    if len(records) > 0 and 0 <= currentDriverIndex < len(records):
        driver, team = records[currentDriverIndex]

        entryName.delete(0, END)
        entryName.insert(0, driver.Driver_Name)

        entryNationality.delete(0, END)
        entryNationality.insert(0, driver.Nationality)

        entryNumber.delete(0, END)
        entryNumber.insert(0, str(driver.Driver_Number))

        entryTeam.delete(0, END)
        entryTeam.insert(0, team.Team_Name)
    loadCurrentPoints()
    loadDriverStats()


def loadCurrentPoints():
    driverName = entryName.get().strip()
    totalPoints = 0

    with Session(engine) as session:
        statement = select(Driver).where(Driver.Driver_Name == driverName)
        driver = session.scalars(statement).first()

        if driver is not None:
            statement = select(Race_Result).where(Race_Result.Driver_ID == driver.Driver_ID)
            resultList = session.scalars(statement).all()

            for result in resultList:
                totalPoints += result.Points

    entryPoints.config(state="normal")
    entryPoints.delete(0, END)
    entryPoints.insert(0, str(totalPoints))
    entryPoints.config(state="readonly")

def loadTeamOptions():
    with Session(engine) as session:
        statement = select(Team).order_by(Team.Team_Name)
        teamList = session.scalars(statement).all()
        teamNames = [team.Team_Name for team in teamList]

    menu = entryTeamFilter["menu"]
    menu.delete(0, "end")

    for teamName in teamNames:
        menu.add_command(label=teamName, command=lambda name=teamName: teamFilterVar.set(name))

    teamFilterVar.set("Select Team")

def loadDriverStats():
    driverName = entryName.get().strip()
    wins = 0
    podiums = 0

    with Session(engine) as session:
        statement = select(Driver).where(Driver.Driver_Name == driverName)
        driver = session.scalars(statement).first()

        if driver is not None:
            statement = select(Race_Result, Race).join(Race, Race_Result.Race_ID == Race.Race_ID).where(Race_Result.Driver_ID == driver.Driver_ID)

            records = session.execute(statement).all()

            for result, race in records:
                if "Sprint" not in race.Race_Name:
                    if result.Finishing_Position == 1:
                        wins += 1

                    if result.Finishing_Position in [1, 2, 3]:
                        podiums += 1

    entryWins.config(state="normal")
    entryWins.delete(0, END)
    entryWins.insert(0, str(wins))
    entryWins.config(state="readonly")

    entryPodiums.config(state="normal")
    entryPodiums.delete(0, END)
    entryPodiums.insert(0, str(podiums))
    entryPodiums.config(state="readonly")

def nextDriver():
    global currentDriverIndex

    with Session(engine) as session:
        statement = select(Driver, Team).join(Team, Driver.Team_ID == Team.Team_ID).order_by(Team.Team_ID, Driver.Driver_Number)
        driverList = session.execute(statement).all()

    if currentDriverIndex < len(driverList) - 1:
        currentDriverIndex += 1
        loadDriver()


def prevDriver():
    global currentDriverIndex

    if currentDriverIndex > 0:
        currentDriverIndex -= 1
        loadDriver()


def clearFields():
    entryName.delete(0, END)
    entryNationality.delete(0, END)
    entryNumber.delete(0, END)
    entryTeam.delete(0, END)



def addDriverWindow():
    window2 = Toplevel(window)
    window2.geometry("350x350")
    window2.title("Add Driver")

    label1 = Label(window2, text="Driver Name")
    label1.place(x=20, y=30)
    entryNewName = Entry(window2, width=25)
    entryNewName.place(x=140, y=30)

    label2 = Label(window2, text="Nationality")
    label2.place(x=20, y=80)
    entryNewNationality = Entry(window2, width=25)
    entryNewNationality.place(x=140, y=80)

    label3 = Label(window2, text="Driver Number")
    label3.place(x=20, y=130)
    entryNewNumber = Entry(window2, width=25)
    entryNewNumber.place(x=140, y=130)

    label4 = Label(window2, text="Team")
    label4.place(x=20, y=180)

    with Session(engine) as session:
        statement = select(Team).order_by(Team.Team_Name)
        teamList = session.scalars(statement).all()
        teamNames = [team.Team_Name for team in teamList]

    newTeamVar = StringVar()

    if len(teamNames) > 0:
        newTeamVar.set(teamNames[0])

    entryNewTeam = OptionMenu(window2, newTeamVar, *teamNames)
    entryNewTeam.config(width=20)
    entryNewTeam.place(x=140, y=175)

    def saveDriver():
        driverName = entryNewName.get().strip()
        nationality = entryNewNationality.get().strip()
        driverNumber = entryNewNumber.get().strip()
        teamName = newTeamVar.get()

        if driverName == "" or nationality == "" or driverNumber == "":
            return

        if not driverNumber.isdigit():
            return

        if len(teamNames) == 0:
            return

        with Session(engine) as session:
            statement = select(Driver).where(Driver.Driver_Number == int(driverNumber))
            existingDriver = session.scalars(statement).first()

            if existingDriver is not None:
                return

            statement = select(Team).where(Team.Team_Name == teamName)
            team = session.scalars(statement).first()

            if team is not None:
                driver = Driver(Driver_Name=driverName,Nationality=nationality,Driver_Number=int(driverNumber),Team_ID=team.Team_ID)

                session.add(driver)
                session.commit()

        loadTeamOptions()
        window2.destroy()

    button1 = Button(window2,text="Save Driver",width=12,command=saveDriver)
    button1.place(x=65, y=260)

    button2 = Button(window2,text="Cancel",width=12,command=window2.destroy)
    button2.place(x=190, y=260)


def updateDriver():
    driverName = entryName.get().strip()
    nationality = entryNationality.get().strip()
    driverNumber = entryNumber.get().strip()
    teamName = entryTeam.get().strip()

    if driverName == "" or nationality == "" or driverNumber == "" or teamName == "":
        return

    if not driverNumber.isdigit():
        return

    with Session(engine) as session:
        statement = select(Driver, Team).join(Team, Driver.Team_ID == Team.Team_ID).order_by(Team.Team_ID, Driver.Driver_Number)

        driverList = session.execute(statement).all()

        if len(driverList) > 0 and 0 <= currentDriverIndex < len(driverList):
            driver, team = driverList[currentDriverIndex]

            teamStatement = select(Team).where(Team.Team_Name == teamName)
            team = session.scalars(teamStatement).first()

            if team is not None:
                driver.Driver_Name = driverName
                driver.Nationality = nationality
                driver.Driver_Number = int(driverNumber)
                driver.Team_ID = team.Team_ID
                session.commit()

def filterDriversByTeam():
    teamName = teamFilterVar.get()

    if teamName == "" or teamName =="Select Team":
        return

    with Session(engine) as session:
        statement = select(Driver, Team).join(Team, Driver.Team_ID == Team.Team_ID).where(Team.Team_Name == teamName).order_by(Driver.Driver_Number)

        records = session.execute(statement).all()
        driverList = []

        for driver, team in records:
            driverList.append((driver.Driver_Number,driver.Driver_Name,driver.Nationality,team.Team_Name))

    displayDialog(window, driverList, "Drivers")


def displayDriverHistory():
    driverName = entryName.get().strip()

    if driverName == "":
        return

    with Session(engine) as session:
        statement = select(Driver).where(Driver.Driver_Name == driverName)
        driver = session.scalars(statement).first()

        if driver is not None:
            statement = select(Race_Result, Race).join(Race, Race_Result.Race_ID == Race.Race_ID).where(Race_Result.Driver_ID == driver.Driver_ID).order_by(Race.Round)

            records = session.execute(statement).all()
            historyList = []

            for result, race in records:
                historyList.append((race.Race_Name,result.Starting_Position,result.Finishing_Position,result.Points,result.Fastest_Lap_Time,result.Status))

            if len(historyList) == 0:
                historyList.append(("No race history available yet", "", "", "", "", ""))

    if driver is not None:
        displayDialog(window, historyList, "Driver History")

def displayDriverStandings():
    with Session(engine) as session:
        statement = select(Driver, Race_Result).join(Race_Result, Driver.Driver_ID == Race_Result.Driver_ID)
        records = session.execute(statement).all()
        standings = {}

        for driver, result in records:
            if driver.Driver_ID not in standings:
                standings[driver.Driver_ID] = [driver.Driver_Name,driver.Driver_Number,0]

            standings[driver.Driver_ID][2] += result.Points

        standingsList = list(standings.values())
        standingsList.sort(key=lambda driver: driver[2], reverse=True)

    displayDialog(window, standingsList, "Driver Standings")


def displayTeamStandings():
    with Session(engine) as session:
        statement = select(Team, Driver, Race_Result).join(Driver, Team.Team_ID == Driver.Team_ID).join(Race_Result, Driver.Driver_ID == Race_Result.Driver_ID)
        records = session.execute(statement).all()
        standings = {}

        for team, driver, result in records:
            if team.Team_ID not in standings:
                standings[team.Team_ID] = [team.Team_Name,0]

            standings[team.Team_ID][1] += result.Points

        standingsList = list(standings.values())
        standingsList.sort(key=lambda team: team[1], reverse=True)

    displayDialog(window, standingsList, "Team Standings")

def insertTeam():
    teamName = entryNewTeam.get().strip()

    if teamName == "":
        return

    with Session(engine) as session:
        statement = select(Team).where(Team.Team_Name == teamName)
        team = session.scalars(statement).first()

        if team is None:
            team = Team(Team_Name=teamName)
            session.add(team)
            session.commit()
            loadTeamOptions()
            entryNewTeam.delete(0, END)


window = Tk()
window.geometry("700x550")
window.title("F1 Driver & Race Results")
window.resizable(False, False)

label1 = Label(window, text="F1 Driver & Race Results", fg="blue", font=("arial", 16, "bold"))
label1.place(x=190, y=20)

label2 = Label(window, text="Driver Details", fg="blue", font=("arial", 12, "bold"))
label2.place(x=25, y=65)

label3 = Label(window, text="Driver Name", fg="blue", font=("arial", 10, "bold"))
label3.place(x=25, y=105)
entryName = Entry(window, width=22)
entryName.place(x=145, y=105)

label4 = Label(window, text="Nationality", fg="blue", font=("arial", 10, "bold"))
label4.place(x=25, y=140)
entryNationality = Entry(window, width=22)
entryNationality.place(x=145, y=140)

label5 = Label(window, text="Driver Number", fg="blue", font=("arial", 10, "bold"))
label5.place(x=25, y=175)
entryNumber = Entry(window, width=22)
entryNumber.place(x=145, y=175)

label6 = Label(window, text="Team", fg="blue", font=("arial", 10, "bold"))
label6.place(x=25, y=210)
entryTeam = Entry(window, width=22)
entryTeam.place(x=145, y=210)

label7 = Label(window, text="Current Points", fg="blue", font=("arial", 10, "bold"))
label7.place(x=25, y=245)
entryPoints = Entry(window, width=22, state="readonly")
entryPoints.place(x=145, y=245)

label8 = Label(window, text="Wins", fg="blue", font=("arial", 10, "bold"))
label8.place(x=25, y=280)
entryWins = Entry(window, width=22, state="readonly")
entryWins.place(x=145, y=280)

label9 = Label(window, text="Podiums", fg="blue", font=("arial", 10, "bold"))
label9.place(x=25, y=315)
entryPodiums = Entry(window, width=22, state="readonly")
entryPodiums.place(x=145, y=315)

label10 = Label(window, text="Team Management", fg="blue", font=("arial", 12, "bold"))
label10.place(x=365, y=65)

label11 = Label(window, text="New Team Name", fg="blue", font=("arial", 10, "bold"))
label11.place(x=365, y=105)
entryNewTeam = Entry(window, width=28)
entryNewTeam.place(x=365, y=130)

label12 = Label(window, text="Filter by Team", fg="blue", font=("arial", 10, "bold"))
label12.place(x=365, y=210)
teamFilterVar = StringVar()
entryTeamFilter = OptionMenu(window, teamFilterVar, "")
entryTeamFilter.config(width=25)
entryTeamFilter.place(x=365, y=235)

label13 = Label(window, text="Application Menu", fg="blue", font=("arial", 12, "bold"))
label13.place(x=365, y=365)

button1 = Button(window, text="Display Teams", width=19, fg="black", font=("arial", 10, "bold"), command=displayTeams)
button1.place(x=365, y=410)

button2 = Button(window, text="Display Drivers", width=19, fg="black", font=("arial", 10, "bold"), command=displayDrivers)
button2.place(x=515, y=410)

button3 = Button(window, text="Display Races", width=19, fg="black", font=("arial", 10, "bold"), command=displayRaces)
button3.place(x=365, y=450)

button4 = Button(window,text="Race Management",width=19,fg="black",font=("arial", 10, "bold"),command=raceManagement)
button4.place(x=515, y=365)

button5 = Button(window, text="Display Race Results", width=19, fg="black", font=("arial", 10, "bold"), command=displayResults)
button5.place(x=515, y=450)

button6 = Button(window, text="Prev", width=8, fg="black", font=("arial", 10, "bold"), command=prevDriver)
button6.place(x=25, y=360)

button7 = Button(window, text="Next", width=8, fg="black", font=("arial", 10, "bold"), command=nextDriver)
button7.place(x=205, y=360)

button8 = Button(window, text="Clear", width=8, fg="black", font=("arial", 10, "bold"), command=clearFields)
button8.place(x=115, y=360)

button9 = Button(window, text="Add Driver", fg="black", font=("arial", 10, "bold"), command=addDriverWindow)
button9.place(x=45, y=395)

button10 = Button(window, text="Update Driver", fg="black", font=("arial", 10, "bold"), command=updateDriver)
button10.place(x=145, y=395)

button11 = Button(window, text="Filter Drivers", fg="black", font=("arial", 10, "bold"), command=filterDriversByTeam)
button11.place(x=365, y=270)

button12 = Button(window, text="Driver Race History", fg="black", font=("arial", 10, "bold"), command=displayDriverHistory)
button12.place(x=365, y=310)

button13 = Button(window, text="Driver Standings", width=19, fg="black", font=("arial", 10, "bold"), command=displayDriverStandings)
button13.place(x=365, y=490)

button14 = Button(window, text="Team Standings", width=19, fg="black", font=("arial", 10, "bold"), command=displayTeamStandings)
button14.place(x=515, y=490)

button15 = Button(window, text="Add Team", fg="black", font=("arial", 10, "bold"), command=insertTeam)
button15.place(x=365, y=165)

loadDriver()
loadTeamOptions()
mainloop()



