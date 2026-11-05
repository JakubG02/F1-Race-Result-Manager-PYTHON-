from tkinter import *

def displayDialog(window, record_list, record_type):
    window2 = Toplevel(window)
    window2.geometry("1000x600")
    window2.title("F1 " + record_type)
    recordList = record_list

    def displayAll():
        for i in range(0, len(recordList)):
            line = ""

            if record_type == "Teams":
                line = str(recordList[i].Team_ID)
                line += "\t\t" + recordList[i].Team_Name

            elif record_type == "Drivers":
                line = str(recordList[i][0])
                line += "\t\t" + recordList[i][1]
                line += "\t\t" + recordList[i][2]
                line += "\t\t" + recordList[i][3]

            elif record_type == "Races":
                line = str(recordList[i].Round)
                line += "\t\t" + recordList[i].Race_Name
                line += "\t\t" + recordList[i].Country
                line += "\t\t" + recordList[i].Race_Date

            elif record_type == "Driver History":
                line = str(recordList[i][0])
                line += "\t\t" + str(recordList[i][1])
                line += "\t\t" + str(recordList[i][2])
                line += "\t\t" + str(recordList[i][3])
                line += "\t\t" + str(recordList[i][4])
                line += "\t\t" + str(recordList[i][5])

            elif record_type == "Driver Standings":
                line = str(i + 1)
                line += "\t\t" + str(recordList[i][1])
                line += "\t\t" + str(recordList[i][0])
                line += "\t\t" + str(recordList[i][2])

            elif record_type == "Team Standings":
                line = str(i + 1)
                line += "\t\t" + str(recordList[i][0])
                line += "\t\t" + str(recordList[i][1])

            elif record_type == "Race Results":
                line = str(recordList[i].Driver_ID)
                line += "\t\t" + str(recordList[i].Race_ID)
                line += "\t\t" + str(recordList[i].Finishing_Position)
                line += "\t\t" + str(recordList[i].Points)
                line += "\t\t" + recordList[i].Status

            line += "\n\n"
            text.insert(END, line)

    def closeEvent():
        window2.destroy()

    button6 = Button(window2, text="Close", fg="black", font=("arial", 12, "bold"), command=closeEvent)
    button6.place(x=10, y=10)

    text = Text(window2, undo=True, height=30, width=115)
    text.place(x=20, y=90)

    if record_type == "Team Standings":
        text.insert(END, "Position\tTeam\t\tPoints\n\n")

    if record_type == "Driver Standings":
        text.insert(END, "Position\tNumber\tDriver\t\tPoints\n\n")

    if record_type == "Driver History":
        text.insert(END, "Grand Prix\t\tStart\t\tFinish\t\tPoints\t\tFastest Lap\t\tStatus\n\n")

    displayAll()


def displayRaceList(window, race_list, view_results):
    window2 = Toplevel(window)
    window2.geometry("600x500")
    window2.title("Select a Grand Prix")
    raceList = race_list

    label1 = Label(window2, text="Select a Grand Prix", font=("arial", 14, "bold"))
    label1.place(x=20, y=20)

    list1 = Listbox(window2, width=65, height=20)
    list1.place(x=20, y=60)

    for race in raceList:
        line = str(race.Round) + ". " + race.Race_Name
        line += " - " + race.Race_Date
        list1.insert(END, line)

    def viewResultsCmd():
        selection = list1.curselection()

        if len(selection) > 0:
            race = raceList[selection[0]]
            view_results(race.Race_ID, race.Race_Name)

    def closeEvent():
        window2.destroy()

    button1 = Button(window2, text="View Results", command=viewResultsCmd)
    button1.place(x=20, y=440)

    button2 = Button(window2, text="Close", command=closeEvent)
    button2.place(x=130, y=440)


def displayRaceResultDialog(window, race_name, result_list):
    window2 = Toplevel(window)
    window2.geometry("1000x600")
    window2.title(race_name + " Results")

    label1 = Label(window2, text=race_name, font=("arial", 16, "bold"))
    label1.place(x=20, y=20)

    text = Text(window2, height=28, width=115)
    text.place(x=20, y=60)

    text.insert(END, "Driver\t\tPosition\tPoints\tFastest Lap\tStatus\n\n")

    if len(result_list) == 0:
        text.insert(END, "No results available for this race.\n")
    else:
        for result in result_list:
            line = str(result[0])
            line += "\t\t" + str(result[1])
            line += "\t" + str(result[2])
            line += "\t" + str(result[3])
            line += "\t" + str(result[4])
            line += "\n\n"
            text.insert(END, line)

    def closeEvent():
        window2.destroy()

    button1 = Button(window2, text="Close", command=closeEvent)
    button1.place(x=20, y=530)
