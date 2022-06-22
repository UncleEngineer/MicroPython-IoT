from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import time

GUI = Tk()
GUI.geometry('1000x900')
GUI.title('Dashboard ระบบ IoT ควบคุม Smart Farm')
GUI.state('zoomed')

# Canvas กระดานวาดภาพ
canvas = Canvas(GUI,width=1500,height=900)
canvas.place(x=0,y=0)

# path = r'C:\Users\Uncle Engineer\Desktop\MicroPython Course\WiFi\farm.png'
# background = ImageTk.PhotoImage(Image.open(path))

# ใส่ background
background = ImageTk.PhotoImage(Image.open('farm.png'))
canvas.create_image(300,200,anchor=NW,image=background)


#############DOOR##############
# วาดหลายเหลี่ยม
canvas.create_polygon([630,426,675,450,675,495,629,470],fill='#0ff717',width=1,outline=None,tags='d1')
# ใส่ข้อความ
canvas.create_text(300,300,text='ประตูฟาร์มกำลังเปิด',fill='green',font=('Angsana New',30,'bold'),tags='d1')
# ใส่ LINE
canvas.create_line(425,320,640,455,fill='grey',width=4,tags='d1')
# canvas.create_line(150,50, 120,100, 50,0, 0,50, smooth=1)

door_state = True #สถานะประตู
def DoorOnOff(event):
    global door_state #เปลี่ยนตัวแปรด้านนอกฟังชั่น
    door_state = not door_state #สลับสถานะ
    canvas.delete('d1')
    if door_state == True:
        canvas.create_polygon([630,426,675,450,675,495,629,470],fill='#0ff717',width=1,outline=None,tags='d1')
        canvas.create_text(300,300,text='ประตูฟาร์มกำลังเปิด',fill='green',font=('Angsana New',30,'bold'),tags='d1')
        canvas.create_line(425,320,640,455,fill='grey',width=4,tags='d1')
    else:
        canvas.create_polygon([630,426,675,450,675,495,629,470],fill='red',width=1,outline=None,tags='d1')
        canvas.create_text(300,300,text='ประตูฟาร์มกำลังปิด',fill='red',font=('Angsana New',30,'bold'),tags='d1')
        canvas.create_line(425,320,640,455,fill='grey',width=4,tags='d1')

################FAN#################
fan = ImageTk.PhotoImage(Image.open('fan.png')) 
canvas.create_image(1063,461,image=fan,tags='img3',anchor=CENTER)

angle = 0

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:	
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image = Image.open('fan.png').rotate(angle)) 
			canvas.create_image(1063,461,image=fan,tags='img3',anchor=CENTER)
		angle += 45
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()


GUI.bind('<Return>',DoorOnOff)
GUI.mainloop()