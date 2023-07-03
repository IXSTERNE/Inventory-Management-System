import tkinter
from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox

window = tkinter.Tk()
window.title("Inventory Management System")

frame = tkinter.Frame(window)
frame.pack()


# Functions
def read_data():
	connect = sqlite3.connect("data.db")
	read = connect.cursor()
	read.execute("""SELECT * FROM products""")
	records = read.fetchall()
	print(records)

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


def add_item():

	add_name = product_name_entry.get()
	add_code = product_code_entry.get()
	add_power = product_power_entry.get()
	add_dim = product_dimension_entry.get()
	add_quant = product_quantity_entry.get()
	add_price = product_price_entry.get()
	add_cat = category_combobox.get()

	if (add_name == '' or add_name == ' ') or (add_code == '' or add_code == ' '):
		messagebox.showinfo("Error", "Please fill name or code")
		return 
	if (add_quant == '' or add_quant == ' ') or (add_price == '' or add_price == ' '):
		messagebox.showinfo("Error", "Please fill quantity or price")
		return
	

	connect = sqlite3.connect("data.db")
	table_create_query = (""" CREATE TABLE IF NOT EXISTS products(
						id integer PRIMARY KEY AUTOINCREMENT, 
						product_name text NOT NULL,
						product_code text NOT NULL,
						power integer,
						dimension text,
						quantity integer NOT NULL,
						price integer NOT NULL,
						category text NOT NULL); """)

	connect.execute(table_create_query)

	# Insert Data
	data_insert_query = '''INSERT INTO products (product_name, product_code, power, 
												dimension, quantity, 
												price, category) VALUES (?, ?, ?, ?, ?, ?, ?)'''

	data_insert_tuple = (add_name, add_code, add_power,
		     			add_dim, add_quant,
				    	add_price, add_cat)
	
	cursor = connect.cursor()
	cursor.execute(data_insert_query, data_insert_tuple)
	connect.commit()
	connect.close()

def search_item():
	print("Search")

def delete_item():
	print("delete")

def update_item():
	print("update")




# Saving item information / First section

product_info_frame = tkinter.LabelFrame(frame, text = "Product")
product_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)


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
	widget.grid_configure(padx = 5, pady = 5)

# Button
add_button = tkinter.Button(product_info_frame, text = "Add Item", command = add_item)
add_button.grid(row = 2, column = 6, padx = 10, pady = 30)




# Table / Second section

table_frame = tkinter.LabelFrame(frame, text = "Table")
table_frame.grid(row = 1, column = 0)

# Table Scrollbar
tree_scroll = Scrollbar(table_frame)
tree_scroll.pack(side = RIGHT, fill = Y)

table = Treeview(table_frame, columns = ('pid', 'pname', 'pcode', 'powe', 'dim', 'quant', 'pr', 'cat'), show = 'headings', yscrollcommand = tree_scroll.set)

# Scrollbar Config
tree_scroll.config(command = table.yview)


table.column("pid", minwidth = 0, width = 40, stretch = False)
table.column("powe", minwidth = 0, width = 100, stretch = False)

table.heading('pid', text = "ID")
table.heading('pname', text = "Product Name")
table.heading('pcode', text = "Product Code")
table.heading('powe', text = "Power (W)")
table.heading('dim', text = "Dimension")
table.heading('quant', text = "Quantity")
table.heading('pr', text = "Price") 
table.heading('cat', text = "Category")

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


read_data()

window.mainloop()