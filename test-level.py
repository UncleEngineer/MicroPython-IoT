from tkinter import *
from tkinter import ttk
import random

GUI = Tk()
GUI.geometry('500x500')
GUI.title('LEVEL')

level_pic = {1:'level1.png',2:'level2.png',3:'level3.png'}

img = PhotoImage(file='level1.png')

LV = Label(GUI,image=img)
LV.pack()

def TempUp(event):
	num = [1,2,3]
	select = random.choice(num)
	print(select)
	new = PhotoImage(file=level_pic[select])
	LV.configure(image=new)
	LV.image = new

GUI.bind('<F1>',TempUp)

GUI.mainloop()