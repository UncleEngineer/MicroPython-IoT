from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *
import os




class ProductIcon:

	def __init__(self):
		self.quantity = None
		self.table_product = None
		self.v_radio = None
		self.button_list = None #เก็บข้อมูลปุ่ม
		self.button_frame = None #ตำแหน่งที่เก็บปุ่ม
		self.function_add = None

	def popup(self):
		# PGUI = Product GUI
		PGUI = Toplevel()
		PGUI.geometry('500x500')
		PGUI.title('ตั้งค่า -> โชว์ไอคอนรายการสินค้า')

		# ตารางสินค้า
		header = ['ID', 'รหัสสินค้า', 'ชื่อสินค้า', 'แสดงไอคอน']
		hwidth = [50,50,200,70]

		self.table_product = ttk.Treeview(PGUI,columns=header, show='headings',height=15)
		self.table_product.pack()

		for hd,hw in zip(header,hwidth):
			self.table_product.column(hd,width=hw)
			self.table_product.heading(hd,text=hd)


		self.table_product.bind('<Double-1>', self.change_status)
		self.insert_table()
		PGUI.mainloop()

	def insert_table(self):
		self.table_product.delete(*self.table_product.get_children())
		data = View_product_table_icon()
		print(data)
		for d in data:
			row = list(d) #convert tuple to list
			
			check = view_product_status(row[0])
			
			# โชว์สถานะของการนำสินค้าไปทำปุ่ม
			if check[-1] == 'show':
				row.append('✔')
			
			self.table_product.insert('','end',value=row)


	def change_status(self,event=None):

		select = self.table_product.selection()
		pid = self.table_product.item(select)['values'][0]
		# print('PID [check]:',pid)

		SGUI = Toplevel() # SGUI = Status GUI
		SGUI.geometry('400x200')

		self.v_radio = StringVar()

		# Radio
		RB1 = ttk.Radiobutton(SGUI,text='โชว์ไอคอน', variable=self.v_radio, value='show',command=lambda x=None:insert_product_status(int(pid),'show'))
		RB2 = ttk.Radiobutton(SGUI,text='ไม่โชว์ไอคอน', variable=self.v_radio, value='',command=lambda x=None:insert_product_status(int(pid),''))
		RB1.pack(pady=20)
		RB2.pack()

		check = view_product_status(pid)
		print('CHECK:',check)
		if check[-1] == 'show':
			RB1.invoke() # ถ้าสถานะเป็น show จะเลือก โชว์ไอคอน
		else:
			RB2.invoke()

		

		def check_close():
			print('closed')
			SGUI.destroy() #ปิดหน้าต่าง
			self.insert_table()
			self.clearbutton()
			self.create_button()


		SGUI.protocol('WM_DELETE_WINDOW', check_close)

		# RB2.invoke() #ตั้งค่า default ของ radio

		# Dropdown

		# dropdown = ttk.Combobox(SGUI, values=['โชว์ไอคอน','ไม่โชว์ไอคอน'])
		# dropdown.pack()
		# dropdown.set('โชว์ไอคอน')

		# dropdown.bind('<<ComboboxSelected>>',lambda x=None: print(dropdown.get()))

		SGUI.mainloop()

	def command(self):
		self.popup()

	# REFRESH หน้าแสดงปุ่ม
	def clearbutton(self):
		print('CLEAR_BUTTON')
		for b in self.button_list.values():
			# b = {'button':B, 'row':row, 'column':column}
			b['button'].grid_forget()
			# b['button'].destroy()

	def create_button(self):
		print('CREATE_BUTTON')
		product = product_icon_list()

		global button_dict
		button_dict = {}

		row = 0
		column = 0
		column_quan = 3 # ปรับค่านี้เพื่อสร้างจำนวนคอลัมน์สินค้า
		for i,(k,v) in enumerate(product.items()):
			if column == column_quan:
				column = 0
				row += 1

			print('IMG:', v['icon'])
			new_icon = PhotoImage(file=v['icon'])
			B = ttk.Button(self.button_frame,text=v['name'],compound='top')
			button_dict[v['id']] = {'button':B, 'row':row, 'column':column}
			B.configure(command=lambda m=k: self.function_add(m))

			B.configure(image=new_icon)
			B.image = new_icon

			B.grid(row=row, column=column)
			column += 1

		self.button_list = button_dict # ทำให้มีการอัพเดตจำนวนปุ่มตัวใหม่


class AddProduct:

	def __init__(self):
		self.v_productid = None
		self.v_title = None
		self.v_price = None
		self.v_imagepath = None
		self.MGUI = None
		self.ProductImage = None
		self.button_list = None #เก็บข้อมูลปุ่ม
		self.button_frame = None #ตำแหน่งที่เก็บปุ่ม
		self.table_product = None
		self.Bsave = None
		self.Bedit = None
		self.Badd = None

	def popup(self):
		self.MGUI = Toplevel()
		self.MGUI.geometry('1200x900+50+50')
		self.MGUI.title('Add Product')

		self.v_productid = StringVar()
		self.v_title = StringVar()
		self.v_price = StringVar()
		self.v_imagepath = StringVar()

		Fadd = Frame(self.MGUI,width=800)

		Fadd.place(x=50,y=50)

		L = Label(Fadd,text=' '*50 ,font=(None,30)).pack() # บรรทัดว่าง
		L = Label(Fadd,text='เพิ่มรายการสินค้า',font=(None,30))
		L.pack(pady=20)

		# -----------------
		L = Label(Fadd,text='รหัสสินค้า',font=(None,20)).pack()
		E1 = ttk.Entry(Fadd,textvariable= self.v_productid,font=(None,20))
		E1.pack(pady=10)

		# -----------------
		L = Label(Fadd,text='ชื่อสินค้า',font=(None,20)).pack()
		E2 = ttk.Entry(Fadd,textvariable= self.v_title,font=(None,20))
		E2.pack(pady=10)

		L = Label(Fadd,text='ราคา',font=(None,20)).pack()
		E3 = ttk.Entry(Fadd,textvariable= self.v_price,font=(None,20))
		E3.pack(pady=10)

		img = PhotoImage(file='default-product.png')
		self.ProductImage = Label(Fadd,textvariable=self.v_imagepath, image=img, compound='top')
		self.ProductImage.pack()

		Bselect = ttk.Button(Fadd, text='เลือกรูปสินค้า ( 120 x 120 px )',command=self.selectfile)
		Bselect.pack(pady=10)

		self.Bsave = ttk.Button(Fadd, text='บันทึก',command=self.saveproduct)
		self.Bsave.pack(pady=10,ipadx=20,ipady=10)

		self.Bedit = ttk.Button(Fadd, text='แก้ไข',command=self.update_product_to_database)
		self.Bedit.pack(pady=10,ipadx=20,ipady=10)
		self.Bedit.pack_forget() #ซ่อนตอนเริ่มต้น

		self.Badd = ttk.Button(Fadd, text='เพิ่ม',command=self.add_button)
		self.Badd.pack(pady=10,ipadx=20,ipady=10)

		###############################
		header = ['ID', 'รหัสสินค้า', 'ชื่อสินค้า', 'ราคา']
		hwidth = [50,100,200,100]

		self.table_product = ttk.Treeview(self.MGUI,columns=header, show='headings',height=30)
		self.table_product.place(x=580,y=50)

		for hd,hw in zip(header,hwidth):
			self.table_product.column(hd,width=hw)
			self.table_product.heading(hd,text=hd)

		self.table_product.bind('<Double-1>', self.update_product)
		self.insert_table() # add product
		self.table_product.bind('<Delete>',self.delete_product_database)
		self.MGUI.mainloop()

	def selectfile(self):
		# self.MGUI.lift()
		filetypes = (
				('PNG', '*.png'),
				('All files', '*.*')
			)
		DIR = os.getcwd() #ตำแหน่งโฟลเดอร์โปรแกรม
		select = filedialog.askopenfilename(title='เลือกไฟล์ภาพ',initialdir=DIR,filetypes=filetypes)
		img = PhotoImage(file=select)
		self.ProductImage.configure(image=img)
		self.ProductImage.image = img # ****

		self.v_imagepath.set(select)
		self.MGUI.focus_force() # โฟกัสหน้าต่างที่ select
		self.MGUI.grab_set()
		'''
		# focus on top level (next time)
		self.lift()
		self.focus_force()
		self.grab_set()
		self.grab_release()
		'''


	def saveproduct(self):
		v1 = self.v_productid.get()
		v2 = self.v_title.get()
		v3 = float(self.v_price.get())
		v4 = self.v_imagepath.get()
		Insert_product(v1,v2,v3,v4)
		self.v_productid.set('')
		self.v_title.set('')
		self.v_price.set('')
		self.v_imagepath.set('')
		View_product()

		# เรียกฟังชั่นเคลียร์ปุ่ม
		self.clearbutton()
		self.create_button()
		self.insert_table()

	def update_product_to_database(self):
		v1 = self.v_productid.get()
		v2 = self.v_title.get()
		v3 = float(self.v_price.get())
		v4 = self.v_imagepath.get()

		update_product(v1,'productid',v1)
		update_product(v1,'title',v2)
		update_product(v1,'price',v3)
		update_product(v1,'image',v4)
		
		self.v_productid.set('')
		self.v_title.set('')
		self.v_price.set('')
		self.v_imagepath.set('')
		self.insert_table()

		# เรียกฟังชั่นเคลียร์ปุ่ม
		self.clearbutton()
		self.create_button()



	def command(self):
		self.popup()


	# REFRESH หน้าแสดงปุ่ม
	def clearbutton(self):
		print('CLEAR_BUTTON')
		for b in self.button_list.values():
			# b = {'button':B, 'row':row, 'column':column}
			b['button'].grid_forget()
			# b['button'].destroy()

	def create_button(self):
		print('CREATE_BUTTON')
		product = product_icon_list()

		global button_dict
		button_dict = {}

		row = 0
		column = 0
		column_quan = 3 # ปรับค่านี้เพื่อสร้างจำนวนคอลัมน์สินค้า
		for i,(k,v) in enumerate(product.items()):
			if column == column_quan:
				column = 0
				row += 1

			print('IMG:', v['icon'])
			new_icon = PhotoImage(file=v['icon'])
			B = ttk.Button(self.button_frame,text=v['name'],compound='top')
			button_dict[v['id']] = {'button':B, 'row':row, 'column':column}
			B.configure(command=lambda m=k: AddMenu(m))

			B.configure(image=new_icon)
			B.image = new_icon

			B.grid(row=row, column=column)
			column += 1

		# self.button_list = button_dict


	def insert_table(self):
		self.table_product.delete(*self.table_product.get_children())
		data = View_product()
		print(data)
		for d in data:
			row = list(d) #convert tuple to list
			self.table_product.insert('','end',value=row[:4])



	def update_product(self,event):
		self.Bsave.pack_forget() # ลบปุ่มเซฟออก
		self.Badd.pack_forget() # ลบปุ่มเพิ่มออก
		self.Bedit.pack(pady=10,ipadx=20,ipady=10) #โชว์ปุ่ม edit
		self.Badd.pack(pady=10,ipadx=20,ipady=10) #โชว์ปุ่มเพิ่มหลัง edit

		select = self.table_product.selection()
		pid = self.table_product.item(select)['values'][1]
		#print(pid)
		data = View_product_single(pid)
		# (11, 'XX-1001', 'ชาเขียว', 50.0, 'C:/Users/Uncle Engineer/Desktop/Python GUI 2022/coffee-shop/cup-of-tea-icon.png')
		print(data)
		self.v_productid.set(data[1])
		self.v_title.set(data[2])
		self.v_price.set(data[3])
		self.v_imagepath.set(data[4])

		img = PhotoImage(file=data[4]) # image path
		self.ProductImage.configure(image=img)
		self.ProductImage.image = img # ****


	def add_button(self):
		self.Bedit.pack_forget()
		self.Badd.pack_forget() # ลบปุ่มเพิ่มออก
		self.Bsave.pack(pady=10,ipadx=20,ipady=10)
		self.Badd.pack(pady=10,ipadx=20,ipady=10)
		self.v_productid.set('')
		self.v_title.set('')
		self.v_price.set('')
		self.v_imagepath.set('')


	def delete_product_database(self,event):
		self.v_productid.set('')
		self.v_title.set('')
		self.v_price.set('')
		self.v_imagepath.set('')

		select = self.table_product.selection()
		pid = self.table_product.item(select)['values'][0]

		Delete_product(pid)
		self.insert_table()



if __name__ == '__main__':
	test = AddProduct()