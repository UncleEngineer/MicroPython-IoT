# GUI-Calculator.py
from tkinter import *
from tkinter import ttk, messagebox

#############DATABASE##############
from memberdb import *
from productdb import *
# View_member()

# import memberdb
# memberdb.View_member()

# import memberdb as db
# db.View_member()
#############FUNCTION##############
from menufunction import *
addproduct = AddProduct()
product_icon = ProductIcon()
#############CSV##############
import csv
from datetime import datetime
def writetocsv(data, filename='data.csv'):
    with open(filename,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

#############GUI##############
GUI = Tk()
GUI.title('โปรแกรมจัดการ layout')
GUI.iconbitmap('loong.ico')
# fullscreen after run
GUI.state('zoomed')

#######STYLE##########
style = ttk.Style()
style.configure('Treeview.Heading',font=(None,12))
style.configure('Treeview', font=(None,10))


######################

W = 1200
H = 600
MW = GUI.winfo_screenwidth() # Monitor Width
MH = GUI.winfo_screenheight() # Monitor Height
SX =  (MW/2) - (W/2) # Start X
SY =  (MH/2) - (H/2) # Start Y
#SY = SY - 50 # diff up

print(MW,MH,SX,SY)
print('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))

############MENUBAR###############
menubar = Menu(GUI)
GUI.config(menu=menubar)
# -----------------------------------------
# File Menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)

def ExportDatabase():
    print('Export Database to CSV')
filemenu.add_command(label='Export',command=ExportDatabase)
filemenu.add_command(label='Exit',command=lambda: GUI.destroy())

# -----------------------------------------
# Member Menu
membermenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Member',menu=membermenu)

# -----------------------------------------
# Product Menu

productmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Product',menu=productmenu)

productmenu.add_command(label='Add Product', command=addproduct.command)

# -----------------------------------------
# Setting

settingmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Setting',menu=settingmenu)

settingmenu.add_command(label='Product Icon', command=product_icon.command)


# -----------------------------------------
# Help Menu
import webbrowser

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
contact_url = 'https://uncle-engineer.com'
helpmenu.add_command(label='Contact US',command=lambda: webbrowser.open(contact_url))

def About():
    ABGUI = Toplevel()
    ABGUI.iconbitmap('loong.ico')
    W = 300
    H = 200
    MW = GUI.winfo_screenwidth() # Monitor Width
    MH = GUI.winfo_screenheight() # Monitor Height
    SX =  (MW/2) - (W/2) # Start X
    SY =  (MH/2) - (H/2) # Start Y
    ABGUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
    L = Label(ABGUI,text='โปรแกรมร้านกาแฟ',fg='green',font=('Angsana New',30)).pack()
    L = Label(ABGUI,text='พัฒนาโดย Uncle Engineer\nhttps://uncle-engineer.com',font=('Angsana New',20)).pack()
    ABGUI.mainloop()

helpmenu.add_command(label='About',command=About)
# -----------------------------------------
#############TAB SETTING##############
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)


T3 = Frame(Tab)
T4 = Frame(Tab)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
icon_tab3 = PhotoImage(file='tab3.png')
icon_tab4 = PhotoImage(file='tab4.png')


Tab.add(T3, text='CAFE',image=icon_tab3,compound='left')
Tab.add(T4, text='Member',image=icon_tab4,compound='left')

############TAB 3 - Coffee ############

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New',15))

CF1 = Frame(T3)
CF1.place(x=50,y=100)

# ROW0
# header = ['No.', 'title', 'quantity','price','total']

allmenu = {}
'''
product = {'latte':{'name':'ลาเต้','price':30},
           'cappuccino':{'name':'คาปูชิโน','price':35},
           'espresso':{'name':'เอสเปรสโซ่','price':40},
           'greentea':{'name':'ชาเขียว','price':20},
           'icetea':{'name':'ชาเย็น','price':15},
           'hottea':{'name':'ชาร้อน','price':10},
           'coco':{'name':'โกโก้','price':50},}
'''

product = product_icon_list()
print(product)


def UpdateTable():
    table.delete(*table.get_children()) # แคลียร์ข้อมูลเก่าในตาราง
    for i,m in enumerate(allmenu.values(),start=1):
        # m = ['ลาเต้', 30, 1, 30]
        table.insert('','end',value=[ i ,m[0],m[1],m[2],m[3] ] )


def AddMenu(name='latte'):
    # name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'],product[name]['price'],1,product[name]['price']]
        
    else:
        # {'latte': ['ลาเต้', 30, 1, 30]}
        quan = allmenu[name][2] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['name'],product[name]['price'], quan ,total]
    print(allmenu)
    # ยอดรวม
    count = sum([ m[3] for m in allmenu.values()])
    v_total.set('{:,.2f}'.format(count))
    UpdateTable()



'''
row = 0        
column = 0         
for i,(k,v) in enumerate(product.items()):
    if column == 3:
               column = 0
               row += 1
    print("B = ttk.Button(CF1,text='{}',image=icon_tab3,compound='top',command=lambda m='{}': AddMenu(m)".format(v['name'],k))
    print('B.grid(row={},column={})'.format(row,column))
    column += 1
    print('--------')
'''

button_dict = {}

row = 0
column = 0
column_quan = 3 # ปรับค่านี้เพื่อสร้างจำนวนคอลัมน์สินค้า
for i,(k,v) in enumerate(product.items()):
    if column == column_quan:
        column = 0
        row += 1
    # print('K:',k)
    print('IMG:', v['icon'])
    new_icon = PhotoImage(file=v['icon'])
    B = ttk.Button(CF1,text=v['name'],compound='top')
    button_dict[v['id']] = {'button':B, 'row':row, 'column':column}
    B.configure(command=lambda m=k: AddMenu(m))

    B.configure(image=new_icon)
    B.image = new_icon

    B.grid(row=row, column=column)
    column += 1


# ส่งค่า dict ของปุ่มและเฟรมไปหาหน้าต่างที่ต้องการอัพเดต
addproduct.button_list = button_dict
addproduct.button_frame = CF1


# ส่งค่า dict ของปุ่มและเฟรมไปหาหน้าต่างที่ต้องการอัพเดต
product_icon.button_list = button_dict
product_icon.button_frame = CF1
product_icon.function_add = AddMenu


print(button_dict)
def testclearbutton(event):
    for b in button_dict.values():
        # b = {'button':B, 'row':row, 'column':column}
        b['button'].grid_forget()

GUI.bind('<F5>',testclearbutton)

# B.grid_forget

'''
B = ttk.Button(CF1,text='ลาเต้',image=icon_tab3,compound='top',command=lambda m='latte': AddMenu(m))
B.grid(row=0,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='คาปูชิโน',image=icon_tab3,compound='top',command=lambda m='cappuccino': AddMenu(m))
B.grid(row=0,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='เอสเปรสโซ่',image=icon_tab3,compound='top',command=lambda m='espresso': AddMenu(m))
B.grid(row=0,column=2,ipadx=20,ipady=10)

# ROW1
B = ttk.Button(CF1,text='ชาเขียว',image=icon_tab3,compound='top',command=lambda m='greentea': AddMenu(m))
B.grid(row=1,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาเย็น',image=icon_tab3,compound='top',command=lambda m='icetea': AddMenu(m))
B.grid(row=1,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาร้อน',image=icon_tab3,compound='top',command=lambda m='hottea': AddMenu(m))
B.grid(row=1,column=2,ipadx=20,ipady=10)
'''



######TABLE#######
CF2 = Frame(T3)
CF2.place(x=500,y=100)

header = ['No.', 'title', 'price','quantity','total']
hwidth = [50,200,100,100,100]

table = ttk.Treeview(CF2,columns=header, show='headings',height=15)
table.pack()

for hd,hw in zip(header,hwidth):
    table.column(hd,width=hw)
    table.heading(hd,text=hd)

# for hd in header:
#     table.heading(hd,text=hd)


L = Label(T3,text='Total:', font=(None,15)).place(x=500,y=450)

v_total = StringVar()
v_total.set('0.0')

LT = Label(T3,textvariable=v_total, font=(None,15))
LT.place(x=600,y=450)

def Reset():
    global allmenu
    allmenu = {}
    table.delete(*table.get_children())
    v_total.set('0.0')
    trstamp = datetime.now().strftime('%y%m%d%H%M%S') #GEN Transaction
    v_transaction.set(trstamp)

B = ttk.Button(T3,text='Clear',command=Reset).place(x=600,y=500)

# Transaction ID
v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S') #GEN Transaction
v_transaction.set(trstamp)
LTR = Label(T3,textvariable=v_transaction,font=(None,10)).place(x=950,y=70)


# Save Button
FB = Frame(T3)
FB.place(x=890,y=450)

def AddTransaction():
    # writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction, stamp, allmenu.values())
    for m in allmenu.values():
        # before: m = ['คาปูชิโน', 35, 1, 35]
        # after: m = ['12341234', '2022-02-17 21:04:19', 'คาปูชิโน', 35, 1, 35]
        m.insert(0,transaction)
        m.insert(1,stamp)
        writetocsv(m,'transaction.csv')
    Reset() #clear data


B = ttk.Button(FB,text='บันทึก',command=AddTransaction)
B.pack(ipadx=30,ipady=20)


##########Search Menu############

FS1 = Frame(T3)
FS1.place(x=300,y=30)
v_search_barcode = StringVar()
Esearch = ttk.Entry(FS1,textvariable=v_search_barcode,font=(None,25,'bold'))
Esearch.grid(row=0,column=0,ipadx=25)

def SearchBarcode(event=None):
    barcode = v_search_barcode.get()
    try:
        res = View_product_single(barcode)
        print(res)
        pid = res[0]
        AddMenu(pid)
    except:
        messagebox.showwarning('Not Found','สินค้าไม่มีในระบบ')
        v_search_barcode.set('')
        Esearch.focus()


Esearch.bind('<Return>',SearchBarcode)
Esearch.bind('<F3>',lambda x: v_search_barcode.set(''))

Bsearch = ttk.Button(FS1,text='ค้นหา',command=SearchBarcode)
Bsearch.grid(row=0,column=1,ipadx=20,ipady=5,padx=10)

# History New Windows

def HistoryWindow(event):
    HIS = Toplevel() # คล้ายกับ GUI = Tk()
    HIS.geometry('750x500')

    L = Label(HIS,text='ประวัติการสั่งซื้อ', font=(None,15)).pack()

    # History
    header = ['ts-id','datetime', 'title', 'price','quantity','total']
    hwidth = [100,100,200,100,100,100]

    table_history = ttk.Treeview(HIS,columns=header, show='headings',height=15)
    table_history.pack()

    for hd,hw in zip(header,hwidth):
        table_history.column(hd,width=hw)
        table_history.heading(hd,text=hd)

    # Update from CSV
    with open('transaction.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file) # file reader
        for row in fr:
            table_history.insert('',0,value=row)

    HIS.mainloop()

GUI.bind('<F1>',HistoryWindow)

#################TAB 4 Member#####################

def ET3(GUI,text,font=('Angsana New',20)):
    v_strvar = StringVar()
    T = Label(GUI,text=text,font=(None,15)).pack()
    E = ttk.Entry(GUI,textvariable=v_strvar,font=font)
    return (E,T,v_strvar)


F41 = Frame(T4) # F41 = Frame in Tab4 , No.1
F41.place(x=50,y=50)

v_membercode = StringVar()
v_membercode.set('M-1001')
v_databasecode = IntVar() # ไว้เก็บเลขฐานข้อมูลที่มีการเลือก


L = Label(T4,text='รหัสสมาชิก:',font=(None,13)).place(x=50,y=20)
LCode = Label(T4,textvariable=v_membercode,font=(None,13)).place(x=150,y=20)

E41,L,v_fullname = ET3(F41,'ชื่อ-สกุล') 
E41.pack()

E42,L,v_tel = ET3(F41,'เบอร์โทร')
E42.pack() 

E43,L,v_usertype = ET3(F41,'ประเภทสมาชิก')
E43.pack()
v_usertype.set('general')

E44,L,v_point = ET3(F41,'คะแนนสะสม')
E44.pack()
v_point.set('0') # ใส่ค่า default ของ point

# E43.bind('<Return>', lambda x: print(v_usertype.get()))

def SaveMember():
    code = v_membercode.get()
    fullname = v_fullname.get()
    tel = v_tel.get()
    usertype = v_usertype.get()
    point = v_point.get()
    print(fullname, tel, usertype, point)
    # writetocsv([code, fullname, tel, usertype, point],'member.csv') #บันทึกสมาชิกใหม่
    Insert_member(code, fullname, tel, usertype, point)
    #table_member.insert('',0,value=[code, fullname, tel, usertype, point])
    UpdateTable_Member()

    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')


BSave = ttk.Button(F41,text='บันทึก',command=SaveMember)
BSave.pack()

def EditMember():
    code = v_databasecode.get() #ดึงรหัสฐานข้อมูลล่าสุดที่เลือก
    print(allmember)
    allmember[code][2] = v_fullname.get()
    allmember[code][3] = v_tel.get()
    allmember[code][4] = v_usertype.get()
    allmember[code][5] = v_point.get()
    # UpdateCSV(list(allmember.values()),'member.csv')
    Update_member(code,'fullname', v_fullname.get())
    Update_member(code,'tel', v_tel.get())
    Update_member(code,'usertype', v_usertype.get())
    Update_member(code,'points', v_point.get()) # * points
    UpdateTable_Member()

    BEdit.state(['disabled']) # ปิดปุ่มแก้
    BSave.state(['!disabled']) # เปิดปุ่มบันทึก
    # set default
    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')

BEdit = ttk.Button(F41,text='แก้ไข',command=EditMember)
BEdit.pack()


def NewMember():
    UpdateTable_Member()
    BEdit.state(['disabled']) # ปิดปุ่มแก้
    BSave.state(['!disabled']) # เปิดปุ่มบันทึก
    # set default
    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')


BNew = ttk.Button(F41,text='New',command=NewMember)
BNew.pack()

#########ตารางโชว์สมาชิก###########
F42 = Frame(T4)
F42.place(x=500,y=100)

header = ['ID', 'Code', 'ชื่อ-สกุล', 'เบอร์โทร','ประเภทสมาชิก','คะแนนสะสม']
hwidth = [50, 50,200,100,100,100]

table_member = ttk.Treeview(F42,columns=header, show='headings',height=15)
table_member.pack()

for hd,hw in zip(header,hwidth):
    table_member.column(hd,width=hw)
    table_member.heading(hd,text=hd)

###########################################
def UpdateCSV(data, filename='data.csv'):
    # data = [[a,b],[a,b]]
    with open(filename,'w',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerows(data) # writerows = replace with list


# Delete ข้อมูลในตารางที่เลือก
def DeleteMember(event=None):
    choice = messagebox.askyesno('ลบรายการ','คุณต้องการลบข้อมูลใช่หรือไม่?')
    print(choice)
    if choice == True:
        select = table_member.selection() #เลือก item 
        print(select)
        if len(select) != 0:
            data = table_member.item(select)['values']
            print(data)
            del allmember[data[0]]
            Delete_member(data[0])
            # UpdateCSV(list(allmember.values()),'member.csv')
            UpdateTable_Member()
        else:
            messagebox.showwarning('ไม่ได้เลือกรายการ','กรุณาเลือกรายการก่อนลบข้อมูล')
    else:
        pass

table_member.bind('<Delete>',DeleteMember)


# Update ข้อมูลสมาชิก
def UpdateMemberInfo(event=None):

    select = table_member.selection() #เลือก item 
    if len(select) != 0:
        code = table_member.item(select)['values'][0]
        v_databasecode.set(code)
        print(allmember[code])
        memberinfo = allmember[code]

        v_membercode.set(memberinfo[1])
        v_fullname.set(memberinfo[2])
        v_tel.set(memberinfo[3])
        v_usertype.set(memberinfo[4])
        v_point.set(memberinfo[5])

        BEdit.state(['!disabled']) # เปิดปุ่มแก้
        BSave.state(['disabled']) # ปิดปุ่มบันทึก
    else:
        messagebox.showwarning('ไม่ได้เลือกรายการ','กรุณาเลือกรายการก่อนแก้ไขข้อมูล')

table_member.bind('<Double-1>',UpdateMemberInfo)

# Update Table
last_member = ''
allmember = {}

def UpdateTable_Member():
    global last_member
    
    fr = View_member()
    table_member.delete(*table_member.get_children()) #clear table
    for row in fr:
        table_member.insert('',0,value=row)
        code = row[0] # ดึงรหัสมา
        allmember[code] = list(row) #convert tuple to list
    
    print('Last ROW:',row)
    last_member = row[1] # select membercode
    # M-1001
    # ['M',1001+1]
    next_member = int(last_member.split('-')[1]) + 1
    v_membercode.set('M-{}'.format(next_member))
    print(allmember)

# POP UP Menu
member_rcmenu = Menu(GUI,tearoff=0) # rcmenu = right click menu
table_member.bind('<Button-3>',lambda event: member_rcmenu.post( event.x_root , event.y_root) )
member_rcmenu.add_command(label='Delete',command=DeleteMember)
member_rcmenu.add_command(label='Update',command=UpdateMemberInfo)

def SearchName():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.google.com/search?q={}'.format(name)
    webbrowser.open(url)

member_rcmenu.add_command(label='Search Name',command=SearchName)

def SearchBCC():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.bbc.co.uk/search?q={}'.format(name)
    webbrowser.open(url)

member_rcmenu.add_command(label='Search BCC',command=SearchBCC)
# https://www.bbc.co.uk/search?q=putin


BEdit.state(['disabled'])
try:
    UpdateTable_Member()
except:
    print('กรุณากรอกข้อมูลอย่างน้อย 1 รายการ')

# import os

# file = os.listdir()
# print(file)

# if 'memberdb.sqlite3' in file:
#     print('OK')
#     UpdateTable_Member()

GUI.mainloop()