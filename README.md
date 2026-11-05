# F1 Race Results Manager

A Python desktop application designed to manage Formula 1 drivers, teams, races and race results using a graphical user interface and a relational database.

This project was developed as part of my **Software Design with AI for Cloud Computing** degree at Technological University of the Shannon (TUS), Athlone.

## Technologies Used

- **Python** – Application logic and functionality
- **Tkinter** – Graphical user interface (GUI)
- **SQLAlchemy ORM** – Database interaction and object-relational mapping
- **SQLite** – Relational database for storing application data

## Features

The application provides the following functionality:

- View and manage Formula 1 driver information
- View Formula 1 teams and their associated drivers
- Browse race information, including circuits, countries and dates
- Display race results for selected races
- Add, update and delete driver records
- Navigate between driver records using First, Next and Previous controls
- Store and retrieve data using SQLAlchemy ORM
- Manage relationships between drivers, teams, races and results

## Database Structure

The application uses four related database tables:

| Table | Description |
|---|---|
| Driver | Stores driver names, nationalities, racing numbers and associated teams |
| Team | Stores Formula 1 team information |
| Race | Stores race names, circuits, countries, dates and round numbers |
| Race_Result | Stores race results, finishing positions, points, fastest laps and race statuses |

SQLAlchemy ORM is used to manage database operations and relationships between these tables.

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/f1-race-results-manager.git
```

**2. Navigate to the project directory**

```bash
cd f1-race-results-manager
```

**3. Install the required dependencies**

```bash
pip install SQLAlchemy
```

Tkinter and SQLite are included with most standard Python installations.

**4. Run the application**

Open the project in PyCharm or another Python IDE and run the main Python application file.

Ensure the database file is located in the directory expected by the application.

## Project Purpose

The aim of this project was to gain practical experience developing a database-driven application using Python.

The project demonstrates:

- Object-oriented programming principles
- Relational database design
- CRUD (Create, Read, Update, Delete) operations
- Database relationships and queries
- Graphical user interface development
- Integration of application logic with persistent data storage

## Future Improvements

Potential future developments include:

- Advanced searching and filtering of race results
- Driver and team performance statistics
- Data visualisation and race result charts
- Support for additional database technologies
- Improved user interface design
