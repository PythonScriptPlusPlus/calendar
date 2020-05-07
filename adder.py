from tkinter import *
tk = Tk()

timeTable = ""
def schedule():
	global timeEnter
	global eventEnter
	global timeTable

	timeTable = timeTable + timeEnter.get()+": " + eventEnter.get() + "\n"
	with open("schedule.csv","a") as f:
		with open("date.txt","r") as d:
			dates = d.read().split(" ")
			hours = timeEnter.get().split(":")
			f.write(str(dates[0])+","+str(dates[1])+","+str(dates[2])+","+str(hours[0])+","+str(hours[1])+","+eventEnter.get()+"\n")
	result["text"] = timeTable

timeEnter = StringVar()
eventEnter = StringVar()

resultF = Frame(tk,bg = "black",bd = 1)
timeF = Frame(tk, bg = "black", bd = 1)
addingF = Frame(tk, bg = "black", bd = 1)

title = Label(tk, text = "Here you can add plans to your calendar",
	width = 45)	
result = Label(resultF, text = timeTable, width = 45, 
	height = 15, bg = "white",anchor=NW,justify=LEFT)

timeText = Label(timeF, text = "Enter time (enter it as hh:mm)", width = 22)
addingText = Label(addingF, text = "Enter name of event",
	width = 22)

time = Entry(timeF, width = 26, textvariable = timeEnter)
adding = Entry(addingF, width = 26, textvariable = eventEnter)

add = Button(tk, text = "Add this to the calendar",width = 45,
	command = schedule)

title.grid(row = 1,column = 1,columnspan = 2)
resultF.grid(row = 2,column = 1,columnspan = 2)
result.pack()

timeF.grid(row = 3, column = 1)
timeText.pack()
time.pack()

addingF.grid(row = 3, column = 2)
addingText.pack()
adding.pack()

add.grid(row = 4,column = 1,columnspan = 2)
tk.mainloop()