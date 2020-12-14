import tkinter
import random

# Create root window
root = tkinter.Tk()

# Change root window background color
root.configure(bg="white")

# Change the Title
root.title("My Super To-Do-List")

# Change the window size
root.geometry("200x500")

# Create an empty list
tasks = []

# For testing purposes list will be occupied
# tasks = ["Do Khan Academy", "Watch Bill Nye", "Do Hindi"]

# Create functions
def update_listbox():
    # Clear the current listbox
    clear_listbox()
    # Populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please add a task"
    
    # After task added delete the content of the input box
    txt_input.delete(0, "end")

def del_all():
    global tasks
    # Clear the tasksk list
    tasks = []
    # Update listbox
    update_listbox()

def delete_one():
    # Get the text of the currently selected item
    task = lb_tasks.get("active")
    # Confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random():
    task = random.choice(tasks)
    lbl_display["text"] = task

def show_number_of_tasks():
    number_of_tasks = len(tasks)
    msg = "Number of Tasks: {}".format(number_of_tasks)
    lbl_display["text"] = msg

lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.pack()

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.pack()

txt_input = tkinter.Entry(root, width=15)
txt_input.pack()

btn_add_task = tkinter.Button(root, text="Add task", fg="black", bg="white", command=add_task)
btn_add_task.pack()

btn_del_all = tkinter.Button(root, text="Delete All", fg="black", bg="white", command=del_all)
btn_del_all.pack()

btn_del_one = tkinter.Button(root, text="Delete", fg="black", bg="white", command=delete_one)
btn_del_one.pack()

btn_sort_asc = tkinter.Button(root, text="Sort ASC", fg="black", bg="white", command=sort_asc)
btn_sort_asc.pack()

btn_sort_desc = tkinter.Button(root, text="Sort DESC", fg="black", bg="white", command=sort_desc)
btn_sort_desc.pack()

btn_choose_random = tkinter.Button(root, text="Choose Random", fg="black", bg="white", command=choose_random)
btn_choose_random.pack()

btn_number_of_tasks = tkinter.Button(root, text="Number of Tasks", fg="black", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.pack()

btn_exit = tkinter.Button(root, text="Exit", fg="black", bg="white", command=exit)
btn_exit.pack()

lb_tasks = tkinter.Listbox(root)
lb_tasks.pack()



# Start the main events loop
root.mainloop()