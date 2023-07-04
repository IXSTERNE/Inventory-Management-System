import tkinter
from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox

window = tkinter.Tk()
window.title("Inventory Management System")

frame = tkinter.Frame(window)
frame.pack()


# Database
def start_database():
	connect = sqlite3.connect("data.db")
	read = connect.cursor()
	read.execute("""CREATE TABLE if not exists products (
			product_name text NOT NULL,
			product_code text,
			product_power integer,
			product_dimension text,
			product_quantity integer NOT NULL,
			product_price integer NOT NULL,
			product_category text)""")
	connect.commit()
	connect.close()


# Functions

def clear_entry():
	row_id_entry.delete(0, END)
	product_name_entry.delete(0, END)
	product_code_entry.delete(0, END)
	product_power_entry.delete(0, END)
	product_dimension_entry.delete(0, END)
	product_quantity_entry.delete(0, END)
	product_price_entry.delete(0, END)
	category_combobox.delete(0, END)


def query_database():
	connect = sqlite3.connect("data.db")
	read = connect.cursor()
	read.execute("""SELECT rowid, * FROM products ORDER BY rowid DESC;""")
	records = read.fetchall()

	for record in records:
		print(record)
	for record in records:
		table.insert(parent = '', index = 0, values = (
			record[0], 
			record[1], 
			record[2], 
			record[3], 
			record[4], 
			record[5], 
			record[6],
			record[7]))

	connect.commit()
	connect.close()

def select_record(event):
	clear_entry()

	selected = table.focus()
	values = table.item(selected, 'values')

	row_id_entry.insert(0, values[0])
	product_name_entry.insert(0, values[1])
	product_code_entry.insert(0, values[2])
	product_power_entry.insert(0, values[3])
	product_dimension_entry.insert(0, values[4])
	product_quantity_entry.insert(0, values[5])
	product_price_entry.insert(0, values[6])
	category_combobox.insert(0, values[7])



def add_item():

	connect = sqlite3.connect("data.db")
	
	read = connect.cursor()
	read.execute("""INSERT INTO products VALUES (
		:prod_name,
		:prod_code,
		:prod_power,
		:prod_dimension,
		:prod_quantity,
		:prod_price,
		:prod_category)""", 
	
	{
		'prod_name' : product_name_entry.get(),
		'prod_code' : product_code_entry.get(),
		'prod_power' : product_power_entry.get(),
		'prod_dimension' : product_dimension_entry.get(),
		'prod_quantity' : product_quantity_entry.get(),
		'prod_price' : product_price_entry.get(),
		'prod_category' : category_combobox.get(),
	})
	
	# Error handling
	if ("product_id_entry" == '' or  'product_id_entry' == ' '):
		messagebox.showinfo("Error", "Please fill id")
		return
	if ('product_name' == '' or 'product_name' == ' ') or ('prodcut_code' == '' or 'product_code' == ' '):
		messagebox.showinfo("Error", "Please fill name or code")
		return 
	if ('product_quantity' == '' or 'product_quantity' == ' ') or ('product_price' == '' or 'product_price' == ' '):
		messagebox.showinfo("Error", "Please fill quantity or price")
		return
	
	connect.commit()
	connect.close()
	
	clear_entry()

	messagebox.showinfo("Nice!", "You have added an item")

	#Refresh treeview
	table.delete(*table.get_children())

	query_database()


def delete_item():

	x = table.selection()[0]
	table.delete(x)

	connect = sqlite3.connect("data.db")
	read = connect.cursor()
	read.execute("""DELETE from products WHERE oid =""" + row_id_entry.get())

	connect.commit()
	connect.close()

	clear_entry()

	messagebox.showinfo("Nice!", "You have deleted an item")

def update_item():
	pass
def search_item():
	pass


# Saving item information / First section

product_info_frame = tkinter.LabelFrame(frame, text = "Product")
product_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

row_id_label = tkinter.Label(product_info_frame, text = "ID").grid(row = 2, column = 0)
product_name_label = tkinter.Label(product_info_frame, text = "Product Name")
product_name_label.grid(row = 0, column = 0)
product_code_label = tkinter.Label(product_info_frame, text = "Product Code")
product_code_label.grid(row = 0, column = 1)
product_power_label = tkinter.Label(product_info_frame, text = "Power (W)")
product_power_label.grid(row = 0, column = 2)
product_dimension_label = tkinter.Label(product_info_frame, text = "Dimension")
product_dimension_label.grid(row = 0, column = 3)
product_quantity_label = tkinter.Label(product_info_frame, text = "Quantity")
product_quantity_label.grid(row = 0, column = 4)
product_price_label = tkinter.Label(product_info_frame, text = "Price")
product_price_label.grid(row = 0, column = 5)

row_id_entry = tkinter.Entry(product_info_frame)
row_id_entry.grid(row = 3, column = 0)
# Can't change the id because it disables the keyboard activity on select
row_id_entry.bind("<Key>", lambda e: "break")
product_name_entry = tkinter.Entry(product_info_frame)
product_code_entry = tkinter.Entry(product_info_frame)
product_power_entry = tkinter.Entry(product_info_frame)
product_dimension_entry = tkinter.Entry(product_info_frame)
product_quantity_entry = tkinter.Entry(product_info_frame)
product_price_entry = tkinter.Entry(product_info_frame)

product_name_entry.grid(row = 1, column = 0)
product_code_entry.grid(row = 1, column = 1)
product_power_entry.grid(row = 1, column = 2)
product_dimension_entry.grid(row = 1, column = 3)
product_quantity_entry.grid(row = 1, column = 4)
product_price_entry.grid(row = 1, column = 5)

# Drop down box
category_label = tkinter.Label(product_info_frame, text = "Category")
category_combobox = Combobox(product_info_frame, values = ["", "Living Room", "Bedroom", "Bathroom", "Eye"])
category_label.grid(row = 0, column = 6)
category_combobox.grid(row = 1, column = 6)


# Padding
for widget in product_info_frame.winfo_children():
	widget.grid_configure(padx = 5)

# Button
add_button = tkinter.Button(product_info_frame, text = "Add Item", command = add_item)
add_button.grid(row = 2, column = 6, padx = 10, pady = 10)




# Table / Second section

table_frame = tkinter.LabelFrame(frame, text = "Table")
table_frame.grid(row = 1, column = 0)

# Table Scrollbar
tree_scroll = Scrollbar(table_frame)
tree_scroll.pack(side = RIGHT, fill = Y)

table = Treeview(table_frame, columns = (
	'pid', 
	'pname', 
	'pcode', 
	'powe', 
	'dim', 
	'quant', 
	'pr', 
	'cat'), show = 'headings', yscrollcommand = tree_scroll.set)

# Scrollbar Config
tree_scroll.config(command = table.yview)

table.column("pid", minwidth = 0, width = 40, stretch = False, anchor = CENTER)
table.column('pname', minwidth = 0, anchor = CENTER)
table.column('pcode', minwidth = 0, anchor = CENTER)
table.column("powe", minwidth = 0, width = 100, stretch = False, anchor = CENTER)
table.column('dim', minwidth = 0, anchor = CENTER)
table.column('quant', minwidth = 0, width = 100, anchor = CENTER)
table.column('pr', minwidth = 0, anchor = CENTER) 
table.column('cat', minwidth = 0, anchor = CENTER)

table.heading('pid', text = "ID")
table.heading('pname', text = "Product Name")
table.heading('pcode', text = "Product Code")
table.heading('powe', text = "Power (W)")
table.heading('dim', text = "Dimension")
table.heading('quant', text = "Quantity")
table.heading('pr', text = "Price")
table.heading('cat', text = "Category")

table.bind("<ButtonRelease-1>", select_record)

table.pack()




# Search bar / Third Section

search_frame = tkinter.LabelFrame(frame, text = "Search")
search_frame.grid(row = 2, column = 0, padx = 20, pady = 20, sticky = "w")

search_product_label = tkinter.Label(search_frame, text = "Search:")
search_product_label.grid(row = 2, column = 0, padx = 20)
search_product_entry = tkinter.Entry(search_frame)
search_product_entry.grid(row = 2, column = 1, padx = 20)

search_category_label = tkinter.Label(search_frame, text = "Category:")
search_category_label.grid(row = 2, column = 2, padx = 20)
search_category_combobox = Combobox(search_frame, values = ["", "Living Room", "Bedroom", "Bathroom", "Eye"])
search_category_combobox.grid(row = 2, column = 3, padx = 20)

#Button
search_button = tkinter.Button(search_frame, text = "Search", command = search_item)
search_button.grid(row = 2, column = 4, padx = 20)


for widget in search_frame.winfo_children():
	widget.grid_configure(pady = 10)




# Update, Delete / Fourth Section

upd_del_frame = tkinter.LabelFrame(frame, text = "Update / Delete")
upd_del_frame.grid(row = 2, column = 0, padx = 20, sticky = "e")

update_button = tkinter.Button(upd_del_frame, text = "Update", command = update_item)
update_button.grid(row = 0, column = 0, padx = 50)

delete_button = tkinter.Button(upd_del_frame, text = "Delete", command = delete_item)
delete_button.grid(row = 0, column = 1, padx = 50)


for widget in upd_del_frame.winfo_children():
	widget.grid_configure(pady = 10)


start_database()
# Query the database
query_database()

window.mainloop()