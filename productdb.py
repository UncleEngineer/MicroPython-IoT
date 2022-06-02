import sqlite3

conn = sqlite3.connect('productdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				productid TEXT,
				title TEXT,
				price REAL,
				image TEXT ) """)

c.execute("""CREATE TABLE IF NOT EXISTS product_status (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				product_id INTEGER,
				status TEXT) """)


def insert_product_status(pid,status):
	#pid = product id
	check = view_product_status(pid)
	if check == None:
		with conn:
			command = 'INSERT INTO product_status VALUES (?,?,?)'
			c.execute(command,(None,pid,status))
		conn.commit()
		print('status saved')
	else:
		print('pid exist!')
		print(check)
		update_product_status(pid,status)

def view_product_status(pid):
	# READ
	with conn:
		command = 'SELECT * FROM product_status WHERE product_id=(?)'
		c.execute(command,([pid]))
		result = c.fetchone()
	return result

def update_product_status(pid,status):
	# UPDATE
	with conn:
		command = 'UPDATE product_status SET status = (?) WHERE product_id=(?)'
		c.execute(command,([status,pid]))
	conn.commit()
	print('updated:',(pid,status))

#################################
def Insert_product(productid,title,price,image):
	# ตรวจสอบ productid ที่มีแล้ว ห้ามซ้ำ
	# CREATE
	with conn:
		command = 'INSERT INTO product VALUES (?,?,?,?,?)' # SQL
		c.execute(command,(None,productid,title,price,image))
	conn.commit() # SAVE DATABASE
	print('saved')
	# add status after insert product
	find = View_product_single(productid)
	insert_product_status(find[0],'show') # show icon ทุกครั้งที่มีการแอด


def View_product():
	# READ
	with conn:
		command = 'SELECT * FROM product'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result

def View_product_table_icon():
	# READ
	with conn:
		command = 'SELECT ID, productid, title FROM product'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result

def View_product_single(productid):
	# READ
	with conn:
		command = 'SELECT * FROM product WHERE productid=(?)'
		c.execute(command,([productid]))
		result = c.fetchone()
	print(result)
	return result

'''
product = {'latte':{'name':'ลาเต้','price':30},
           'cappuccino':{'name':'คาปูชิโน','price':35},
           'espresso':{'name':'เอสเปรสโซ่','price':40},
           'greentea':{'name':'ชาเขียว','price':20},
           'icetea':{'name':'ชาเย็น','price':15},
           'hottea':{'name':'ชาร้อน','price':10},
           'coco':{'name':'โกโก้','price':50},}
'''
def product_icon_list():
	with conn:
		command = 'SELECT * FROM product'
		c.execute(command)
		product = c.fetchall()

	with conn:
		command = "SELECT * FROM product_status WHERE status = 'show'"
		c.execute(command)
		status = c.fetchall()

	result = [] 

	for s in status:
		for p in product:
			if s[1] == p[0]:
				#print(p,s[-1])
				result.append(p)

	result_dict = {}
	# print(result)
	# (1, 'A-1001', 'เอสเพรสโซ่', 25.0, 'C:/Users/Uncle Engineer/Desktop/Live/PythonGUI-10.png')
	for r in result:
		result_dict[r[0]] = {'id':r[0],'productid':r[1],'name':r[2],'price':r[3],'icon':r[4]}

	return result_dict


def update_product(pid,field,data):
	# UPDATE
	with conn:
		command = 'UPDATE product SET {} = (?) WHERE productid=(?)'.format(field)
		c.execute(command,([data,pid]))
	conn.commit()
	print('updated:',(pid,data))


def Delete_product(ID):
	# DELETE
	with conn:
		command = 'DELETE FROM product WHERE ID=(?)'
		c.execute(command,([ID]))
	conn.commit()
	print('deleted')


if __name__ == '__main__':
	x = product_icon_list()
	print(x)
	# ฟังชั่นนี้เอาไว้เช็คว่าตอนนี้ไฟล์ที่กำลังรันนี้อยู่ในไฟล์จริงหรือไม่?
	#Insert_product('CF-1002','เอสเปรสโซ่',45, r'C:\Image\latte.png')
	# r'/Users/uncleengineer/Desktop/GUI/Image/a.png'
	# View_product()
	# View_product_table_icon()
	# insert_product_status(1,'show')
	# print(view_product_status(1))
	