from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from threading import Thread

GUI = Tk()
GUI.geometry('500x500')
GUI.title('LEVEL')

level_pic = {1:'level1.png',2:'level2.png',3:'level3.png'}

img = PhotoImage(file='level1.png')

# LV = Label(GUI,image=img)
# LV.pack()

def TempUp(event):
	num = [1,2,3]
	select = random.choice(num)
	print(select)
	new = PhotoImage(file=level_pic[select])
	LV.configure(image=new)
	LV.image = new


canvas= Canvas(GUI, width= 600, height= 400)
canvas.place(x=0,y=0)

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("farm.png"))
canvas.create_image(10,10,anchor=NW,image=img)

canvas.create_text(300, 50, tags='text1', text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))


count = 0

def change_text(event):
	global count
	count += 1
	text = 'สวัสดี: {}'.format(count)
	canvas.delete('text1')
	canvas.create_text(300, 50, tags='text1', text=text, fill="black", font=('Angsana New',40,'bold'))

# canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill='white',outline='gray')

create_circle(100, 100, 20, canvas)


# polygon.create_polygon([150,75,225,0,300,75,225,150],     outline='gray', 
#             fill='gray', width=2)

oval = canvas.create_polygon([150,75, 225,0, 300,75],fill='white',outline='gray')


def resize_image(file,size=50,rotate=0):
	fixed_height = size
	image = Image.open(file)
	height_percent = (fixed_height / float(image.size[1]))
	width_size = int((float(image.size[0]) * float(height_percent)))
	image = image.resize((width_size, fixed_height))
	return image


# # img = Image.open("pin.png")

# print(img.size)
# # image = img.resize((50, 50))
img2= ImageTk.PhotoImage(resize_image('pin.png'))
canvas.create_image(50,50,image=img2,tags='img2')



fan = ImageTk.PhotoImage(Image.open('fan.png')) 
canvas.create_image(200,200,image=fan,tags='img3')

import time

angle = 0

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:	
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image = Image.open('fan.png').rotate(angle)) 
			canvas.create_image(200,200,image=fan,tags='img3')
		angle += 20
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()


Label(GUI,text='hello world').place(x=100,y=100)

GUI.bind('<Return>',change_text)
GUI.bind('<F1>',lambda x: canvas.delete('img2'))

GUI.mainloop()
