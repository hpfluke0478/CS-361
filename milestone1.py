from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

root = Tk()
root.title('Milestone #1 - Minimal TaskMaster')
root.geometry("500x500")
frame = Frame(root)
frame.pack(pady = 10)

def new_task():
    task = uinput.get()
    if task == "":
        messagebox.showwarning("Please type in task entry field.")
    else:
        task_list.insert(END, task)
        uinput.delete(0, "end")

def delete():
    task_list.delete(ANCHOR)

task_list = Listbox(
    frame,
    width = 20,
    height = 10,
    font = ('Times', 15),
    bd = 0
)
task_list.pack(side = LEFT, fill = BOTH)

tasks = [
    'Homework',
    'Chores',
    'Groceries'
]

for item in tasks:
    task_list.insert(END, item)

scroll = Scrollbar(frame)
scroll.pack(side = RIGHT, fill = BOTH)
task_list.config(yscrollcommand = scroll.set)
scroll.config(command=task_list.yview)

uinput = Entry(
    root, 
    font = ('times', 20)
)
uinput.pack(pady = 10)

new_button = Frame(root)
new_button.pack(pady=20)

add_button = Button(
    new_button,
    text='Add Task',
    font=('times 10'),
    padx=20,
    pady=10,
    command=new_task
)
add_button.pack(fill=BOTH, expand=True, side=LEFT)

delete_button = Button(
    new_button,
    text='Delete Task',
    font=('times 10'),
    padx=20,
    pady=10,
    command=delete
)
delete_button.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
