from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Lalith - Treeview")
root.geometry("500x600")

my_tree = ttk.Treeview(root)

# Define our columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favorite Pizza", anchor=W, width=120)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Add Data
data = [
    ["Rajesh", 1, "Chicken"],
    ["Premalatha", 2, "Vegetable"]
]

global count
count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]))
    count += 1

# Add data
# my_tree.insert(parent='', index='end', iid=0, text="", values=("Rajesh", 1, "Chicken"))
# my_tree.insert(parent='', index='end', iid=1, text="", values=("Premalatha", 2, "Vegetable"))
# my_tree.insert(parent='', index='end', iid=2, text="", values=("Lalith", 1.2, "Cheese"))
# my_tree.move('2', '0', '0')

# Pack to the screen
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

# Labels
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

# Entry Boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

# Add Record
def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()))
    count += 1

    # Clear the boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

# Remove All Records
def remove_all_records():
    for record in my_tree.get_children():
        my_tree.delete(record)

# Remove Selected Record
def remove_selected_record():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# Remove Many Selected Records
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

# Buttons
add_record = Button(root, text="Add Record", command=add_record)
add_record.pack(pady=20)

# Remove All Records
remove_all_records = Button(root, text="Remove All Records", command=remove_all_records)
remove_all_records.pack(pady=10)

# Remove Selected Record
remove_selected_record = Button(root, text="Remove Selected Record", command=remove_selected_record)
remove_selected_record.pack(pady=10)

# Remove Many Selected
remove_many = Button(root, text="Remove Many Selected Records", command=remove_many)
remove_many.pack(pady=10)

root.mainloop()