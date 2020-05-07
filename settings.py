from tkinter import *
from tkinter import messagebox
tk = Tk()

def getRes():
	global xRes
	global yRes
	messagebox.showwarning("Please, pay attention!","Please, restart the app, to apply changes")
	with open("settings.csv","a") as f:
		f.write("\nresolution,"+str(xRes.get())+","+str(yRes.get()))

xRes = StringVar()
yRes = StringVar()

resTitle = Label(tk,text = "Set resolution for Calendar",font=('InriaSans-Regular',20))
xInput = Entry(tk,width=37,font=30, textvariable = xRes)
cross = Label(tk,text = "x",font=('InriaSans-Regular',10))
yInput = Entry(tk,width=37,font=30, textvariable = yRes)
Apply = Button(tk,text = "Apply",font = 40,width=36, command=getRes)
tk.title("settings")

resTitle.pack()
xInput.pack()
cross.pack()
yInput.pack()
Apply.pack()
tk.mainloop()