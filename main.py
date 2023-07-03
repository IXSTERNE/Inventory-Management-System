import tkinter
from tkinter import ttk
from random import choice

window = tkinter.Tk()
window.title("Inventory Management System")

frame = tkinter.Frame(window)
frame.pack()




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
category_label= tkinter.Label(product_info_frame, text = "Category")
category_combobox = ttk.Combobox(product_info_frame, values = ["", "Living Room", "Bedroom", "Bathroom", "Eye"])
category_label.grid(row = 0, column = 6)
category_combobox.grid(row = 1, column = 6)


# Padding
for widget in product_info_frame.winfo_children():
	widget.grid_configure(padx = 5, pady = 5)

# Button
add_button = tkinter.Button(product_info_frame, text = "Add Item")
add_button.grid(row = 2, column = 6, padx = 10, pady = 30)




# Table / Second section

table_frame = tkinter.LabelFrame(frame, text = "Table")
table_frame.grid(row = 1, column = 0)


product_names = ['John', 'Jim', 'Jimbo', 'Jack', 'Jocelyn']
product_codes = ['Craig', 'Courtney', 'Camus', 'Connor', 'Coloumb']
powers = ['15W', '16W', '18W', '15W', '28W']
dimensions = ['400', '500', '100', '200', '1000']
quantities = ['28', '17', '12', '78', '5']
prices = ['10000', '20000', '30000', '50000', '19000']
categories = ['Bedroom', 'Living Room', 'Eye', 'Kitchen', 'Bathroom']


table = ttk.Treeview(table_frame, columns = ('pname', 'pcode', 'powe', 'dim', 'quant', 'pr', 'cat'), show = 'headings')


table.heading('pname', text = "Product Name")
table.heading('pcode', text = "Product Code")
table.heading('powe', text = "Power (W)")
table.heading('dim', text = "Dimension")
table.heading('quant', text = "Quantity")
table.heading('pr', text = "Price") 
table.heading('cat', text = "Category")

table.grid()

# Table insert
for i in range(len(product_names)):
	pname = product_names[i]
	pcode =  product_codes[i]
	powe = powers[i]
	dim = dimensions[i]
	quant = quantities[i]
	pr = prices[i]
	cat = categories[i]

	data = (pname, pcode, powe, dim, quant, pr, cat)
	table.insert(parent = '', index = 0, values = data)




# Search bar / Third Section

search_frame = tkinter.LabelFrame(frame, text = "Search")
search_frame.grid(row = 2, column = 0, padx = 20, pady = 20, sticky = "w")


search_product_label = tkinter.Label(search_frame, text = "Search:")
search_product_label.grid(row = 2, column = 0, padx = 20)
search_product_entry = tkinter.Entry(search_frame)
search_product_entry.grid(row = 2, column = 1, padx = 20)

search_category_label = tkinter.Label(search_frame, text = "Category:")
search_category_label.grid(row = 2, column = 2, padx = 20)
search_category_combobox = ttk.Combobox(search_frame, values = ["", "Living Room", "Bedroom", "Bathroom", "Eye"])
search_category_combobox.grid(row = 2, column = 3, padx = 20)

#Button
search_button = tkinter.Button(search_frame, text = "Search")
search_button.grid(row = 2, column = 4, padx = 20)


for widget in search_frame.winfo_children():
	widget.grid_configure(pady = 10)




# Update, Delete / Fourth Section

upd_del_frame = tkinter.LabelFrame(frame, text = "Update / Delete")
upd_del_frame.grid(row = 2, column = 0, padx = 20, sticky = "e")

update_button = tkinter.Button(upd_del_frame, text = "Update")
update_button.grid(row = 0, column = 0, padx = 50)

delete_button = tkinter.Button(upd_del_frame, text = "Delete")
delete_button.grid(row = 0, column = 1, padx = 50)


for widget in upd_del_frame.winfo_children():
	widget.grid_configure(pady = 10)






window.mainloop()