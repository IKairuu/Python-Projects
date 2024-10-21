from background import Background_Process
import tkinter as tk
from tkinter import messagebox

class User_Input(Background_Process):
    def __init__(gui):
        gui.root = tk.Tk()
        gui.process = Background_Process()
        gui.root.title("Task Manager")
        gui.root.geometry("400x400")
        gui.root.resizable(width=False, height=False)
        gui.dictionary = gui.process.create_dictionary()
        gui.addTask = False
        gui.viewTask = False
        gui.deleteTask = False
        gui.markTask = False
        gui.initDel = False
        
        gui.menubar = tk.Menu(gui.root)
        gui.actionsMenu = tk.Menu(gui.menubar, tearoff=0)
        gui.actionsMenu.add_command(label="Add Task", font=("Arial", 10), command=gui.add_task)
        gui.actionsMenu.add_command(label="View Task", font=("Arial", 10), command=gui.view_task_main)
        gui.actionsMenu.add_command(label="Delete Task", font=("Arial", 10), command=gui.delete_task)
        gui.actionsMenu.add_command(label="Exit", font=("Arial", 10), command=exit)
        gui.menubar.add_cascade(menu=gui.actionsMenu, label="Actions", font=("Arial", 10))
        gui.root.config(menu=gui.menubar)
        
        gui.options()
        
        gui.root.mainloop()
        
    def options(gui):
        gui.optionsFrame = tk.Frame(gui.root)
        gui.optionsFrame.pack()
        
        gui.header = tk.Label(gui.optionsFrame, text="TASK MANAGER", font=("Courier", 30))
        gui.header.pack()
        
        gui.add_taskButton = tk.Button(gui.optionsFrame, text="ADD TASK", font=("Arial", 20), width=70, command= gui.add_task, activeforeground="White", activebackground="Blue", cursor="hand2")
        gui.add_taskButton.pack(padx=10,pady=5)
        
        gui.view_taskButton = tk.Button(gui.optionsFrame, text="VIEW TASK", font=("Arial", 20), width=70, command= gui.view_task_main, activeforeground="White", activebackground="Blue", cursor="hand2")
        gui.view_taskButton.pack(padx=10,pady=5)
        
        gui.delete_taskButton = tk.Button(gui.optionsFrame, text="DELETE TASK", font=("Arial", 20), width=70, command=gui.delete_task, activeforeground="White", activebackground="Blue", cursor="hand2")
        gui.delete_taskButton.pack(padx=10,pady=5)
        
        gui.exit_taskButton = tk.Button(gui.optionsFrame, text="EXIT",command=exit, font=("Arial", 20), width=70, activeforeground="White", activebackground="Blue", cursor="hand2")
        gui.exit_taskButton.pack(padx=10,pady=5)
    
    def destroy_frame(gui):
        if gui.addTask:
            gui.headerFrame.destroy()
            gui.add_taskFrame.destroy()
            gui.options()
        elif gui.viewTask:
            gui.viewTaskFrame.destroy()
            gui.buttonFrame.destroy()
            gui.dueTaskFrame.destroy()
            gui.options()
        elif gui.markTask:
            gui.markTaskFrame.destroy()
            gui.frameOfButtons.destroy()
            gui.view_task_main()
        elif gui.deleteTask:
            gui.viewTaskFrame.destroy()
            gui.deleteButtons.destroy()
            gui.options()
        elif gui.initDel:
            gui.deleteHeaderFrame.destroy()
            gui.checkBoxFrame.destroy()
            gui.button_frame.destroy()
            gui.delete_task()
    
    def save_task(gui):
        gui.process.listName.append(gui.nameLabel.get())
        gui.process.listDay.append(gui.dayLabel.get())
        gui.process.listMonth.append(gui.monthLabel.get())
        gui.process.listYear.append(gui.yearLabel.get())
        gui.process.listMark.append("Undone")
        gui.process.listCheck.append(0)
        gui.process.dictionary.update({gui.nameLabel.get(): 0})
        gui.process.save_files()
        gui.destroy_frame()
    
    def add_task(gui):
        gui.addTask = True
        gui.viewTask = False
        gui.deleteTask = False
        gui.markTask = False
        gui.initDel = False
        gui.optionsFrame.forget()
        gui.headerFrame = tk.Frame(gui.root)
        gui.headerFrame.pack()
        gui.header = tk.Label(gui.headerFrame, text="TASK MANAGER", font=("Courier", 30))
        gui.header.pack()
        gui.add_taskFrame = tk.Frame(gui.root)
        gui.add_taskFrame.pack(fill="x")
        gui.root.columnconfigure(0, weight=5)
        gui.root.columnconfigure(1, weight=5)
        gui.invalidFrame = tk.Frame(gui.root)
        gui.invalidFrame.pack()
        gui.invalid = True
        
        gui.nameInput = tk.Label(gui.add_taskFrame, text="Enter Task Name: ")
        gui.nameInput.grid(row=1, column=0)
        gui.nameLabel = tk.Entry(gui.add_taskFrame, width=25)
        gui.nameLabel.grid(row=1, column=1)
        gui.dayInput = tk.Label(gui.add_taskFrame, text="Enter Task Due day(1-30): ")
        gui.dayInput.grid(row=2, column=0)
        gui.dayLabel = tk.Entry(gui.add_taskFrame, width=25)
        gui.dayLabel.grid(row=2, column=1)
        gui.dayInput = tk.Label(gui.add_taskFrame, text="Enter Task Due month(1-12): ")
        gui.dayInput.grid(row=3, column=0)
        gui.monthLabel = tk.Entry(gui.add_taskFrame, width=25)
        gui.monthLabel.grid(row=3, column=1)
        gui.yearInput = tk.Label(gui.add_taskFrame, text="Enter Task Due year: ")
        gui.yearInput.grid(row=4, column=0)
        gui.yearLabel = tk.Entry(gui.add_taskFrame, width=25)
        gui.yearLabel.grid(row=4, column=1)
                  
        gui.back = tk.Button(gui.add_taskFrame, text="BACK", height=2, width=10, font=("Arial", 10), command= gui.destroy_frame)
        gui.back.grid(padx=10, pady=10,row=5, column=0, sticky=tk.W+tk.E)
        gui.confirm = tk.Button(gui.add_taskFrame, text="CONFIRM", height=2, width=10, font=("Arial", 10), command=gui.check_input)
        gui.confirm.grid(padx=10, pady=10,row=5, column=1, sticky=tk.W+tk.E)
    
    def check_input(gui):
        try:
            if len(gui.process.listName) > 10:
                messagebox.showerror(title="Error", message="Task limit reached")
            elif len(gui.nameLabel.get()) > 10 or len(gui.nameLabel.get()) <= 0:
                messagebox.showerror(title="Input Error", message="Maximum of 10 characters")
            elif gui.nameLabel.get() in gui.process.dictionary:
                messagebox.showerror(title="Task Name", message="Task Name already exist")
            elif int(gui.dayLabel.get()) > 30 or int(gui.dayLabel.get()) <= 0:
                messagebox.showerror(title="Input Error", message="Incorrect Input\nInput 1-30 days")
            elif int(gui.monthLabel.get()) > 12 or int(gui.monthLabel.get()) <= 0:
                messagebox.showerror(title="Input Error", message="Incorrect Input\nInput 1-12 month")
            elif len(gui.yearLabel.get()) != 4:
                messagebox.showerror(title="Input Error", message="Incorrect Year Input")
            else:
                gui.save_task()
        except:
            messagebox.showerror(title="Inpur Error", message="Invalid Input")
            
    def view_task(gui):
        gui.addTask = False
        gui.viewTask = True
        gui.deleteTask = False
        gui.markTask = False
        gui.initDel = False
        gui.optionsFrame.destroy()
        gui.viewTaskFrame = tk.Frame(gui.root)
        gui.viewTaskFrame.pack()
        
        gui.viewTaskTitle = tk.Label(gui.viewTaskFrame, text="TASKS", font=("Courier", 30))
        gui.viewTaskTitle.pack()
        
        gui.scroll = tk.Scrollbar(gui.viewTaskFrame, orient='vertical')
        gui.scroll.pack(side="right", fill="y")
        
        gui.taskLists = tk.Text(gui.viewTaskFrame, width=40, height=5, yscrollcommand=gui.scroll.set)
        for num in range(len(gui.process.listDay)):
            gui.taskLists.insert(tk.END, f'{gui.process.listName[num]}\t\t{gui.process.listDay[num]}/{gui.process.listMonth[num]}/{gui.process.listYear[num]}\t\t{gui.process.listMark[num]}\n')
        gui.scroll.config(command=gui.taskLists.yview)
        gui.taskLists.pack()
    
    def show_due_task(gui):
        gui.process.due_tasks()
        gui.dueTaskFrame = tk.Frame(gui.root)
        gui.dueTaskFrame.pack()
        
        gui.headerDueTask =tk.Label(gui.dueTaskFrame, text="DUE TASKS", font=("Arial bold", 10))
        gui.headerDueTask.pack()
        
        gui.show_due_task_scroll = tk.Scrollbar(gui.dueTaskFrame, orient="vertical")
        gui.show_due_task_scroll.pack(fill="y", side="right")
        
        gui.showTask = tk.Text(gui.dueTaskFrame, width=40, height=5, yscrollcommand=gui.show_due_task_scroll.set)
        gui.showTask.pack()
        for index, x in enumerate(gui.process.dueTasks):
            gui.showTask.insert(tk.END, f"{x['name']}\t\t{x['day']}/{x['month']}/{x['year']}\t\t{x['mark']}\n") 
        gui.show_due_task_scroll.config(command=gui.showTask.yview)
    
    def view_task_main(gui):
        gui.view_task()
        gui.buttonFrame = tk.Frame(gui.root)
        gui.buttonFrame.pack()
        gui.root.columnconfigure(0, weight=5)
        gui.root.columnconfigure(1, weight=5)
        
        gui.back = tk.Button(gui.buttonFrame, text="BACK", height=2, width=20, command=gui.destroy_frame)
        gui.back.grid(row=0, column=0, sticky=tk.W+tk.E)
        gui.mark = tk.Button(gui.buttonFrame, text="MARK", height=2, width=20, command=gui.mark_task)
        gui.mark.grid(row=0, column=1, sticky=tk.W+tk.E)
        
        gui.show_due_task() #due tasks HERE
    
    def mark_task(gui):
        gui.addTask = False
        gui.viewTask = False
        gui.deleteTask = False
        gui.markTask = True
        gui.initDel = False
        gui.viewTaskFrame.destroy()
        gui.buttonFrame.destroy()
        gui.dueTaskFrame.destroy()
        gui.markTaskFrame = tk.Frame(gui.root)
        gui.markTaskFrame.pack()
        gui.frameOfButtons = tk.Frame(gui.root)
        gui.frameOfButtons.pack()
        gui.frameOfButtons.columnconfigure(0, weight=5)
        gui.frameOfButtons.columnconfigure(1, weight=5)
        gui.boxes = []
        gui.markHeader = tk.Label(gui.markTaskFrame, text="TASKS", font=("Courier", 30))
        gui.markHeader.grid(row=0, sticky=tk.W+tk.E)
        
        for tasks in gui.process.dictionary.keys():
            gui.check = tk.IntVar(value=gui.process.dictionary[tasks]) #gets the value of the tasks either 1 or 0
            gui.checkButton = tk.Checkbutton(gui.markTaskFrame, text=tasks, variable=gui.check, font=("Courier", 10)) #creates a checkbox list 
            gui.checkButton.grid(row=len(gui.boxes)+1) #positions the checkbox in respective order 
            gui.boxes.append({"tasks":tasks, "state":gui.check}) #appends every element in the dictionary in order to create the checklist
        gui.backButton = tk.Button(gui.frameOfButtons, text="BACK", font=("Arial", 15), width=15, command=gui.destroy_frame).grid(row=0, column=0, sticky=tk.W)
        gui.confirmButton = tk.Button(gui.frameOfButtons, command=lambda:gui.initial_check_task(gui.boxes), text="CONFIRM", font=("Arial", 15), width=15).grid(row=0, column=1, sticky=tk.E)
        
    def delete_task(gui):
        gui.view_task()
        gui.addTask = False
        gui.viewTask = False
        gui.deleteTask = True
        gui.markTask = False
        gui.initDel = False
        gui.deleteButtons = tk.Frame(gui.root)
        gui.deleteButtons.pack()
        
        gui.buttonBack = tk.Button(gui.deleteButtons, text="BACK", height=2, width=15, command=gui.destroy_frame).grid(row=2,column=0, sticky=tk.W)
        gui.buttonDelete = tk.Button(gui.deleteButtons, text="DELETE", height=2, width=15, command=gui.initial_delete_task).grid(row=2,column=1)
        gui.buttonDeleteAll = tk.Button(gui.deleteButtons, text="DELETE ALL", height=2, width=15, command=gui.clear_all_tasks).grid(row=2,column=2, sticky=tk.E)
    
    def clear_all_tasks(gui):
        gui.process.listDay.clear()
        gui.process.listMark.clear()
        gui.process.listMonth.clear()
        gui.process.listName.clear()
        gui.process.listYear.clear()
        gui.process.listCheck.clear()
        gui.process.dictionary.clear() #possible to be shortened
        gui.process.save_files()
        gui.destroy_frame()
    
    def initial_delete_task(gui):
        gui.addTask = False
        gui.viewTask = False
        gui.deleteTask = False
        gui.markTask = False
        gui.initDel = True
        gui.viewTaskFrame.destroy()
        gui.deleteButtons.destroy()
        gui.deleteHeaderFrame = tk.Frame(gui.root)
        gui.deleteHeaderFrame.pack()
        gui.deleteHeader = tk.Label(gui.deleteHeaderFrame, text="TASKS", font=("Courier", 30)).pack()
        gui.checkBoxFrame = tk.Frame(gui.root)
        gui.checkBoxFrame.pack()
        gui.deletedTasks = []
        for index, tasks in enumerate(gui.process.dictionary.keys()):
            gui.deleteCheckState = tk.IntVar(value=0)
            gui.checkBox = tk.Checkbutton(gui.checkBoxFrame, text=tasks, variable=gui.deleteCheckState, font=("Courier", 10) ).grid(row=index)
            gui.deletedTasks.append({"tasks":gui.process.listName[index], "state":gui.deleteCheckState})
        gui.button_frame = tk.Frame(gui.root)
        gui.button_frame.pack()
        gui.back_button = tk.Button(gui.button_frame, text="BACK", font=("Arial", 10), command=gui.destroy_frame, height=2, width=20).grid(row=0, column=0, sticky=tk.W)
        gui.delete_button = tk.Button(gui.button_frame, text="DELETE", font=("Arial", 10), command=lambda:gui.empty_list(gui.deletedTasks), height=2, width=20).grid(row=0, column=1, sticky=tk.E)
    
    def empty_list(gui, deletedTasks):
        for index, x in enumerate(deletedTasks):
            index = 0
            if x["state"].get():
                gui.process.dictionary.pop(x["tasks"])
                for y in gui.process.listName:
                    if x["tasks"] == y:
                        break
                    index += 1
                del gui.process.listName[index]
                del gui.process.listDay[index]
                del gui.process.listMonth[index]
                del gui.process.listYear[index]
                del gui.process.listMark[index]
                del gui.process.listCheck[index]
        gui.dueTasks = gui.process.due_tasks() #PROBLEM
        gui.process.save_files()
        gui.destroy_frame()
    
    def initial_check_task(gui, boxes):
        for index, x in enumerate(boxes):
            if x["state"].get():
                gui.process.dictionary[gui.process.listName[index]] = 1
                gui.process.listCheck[index] = 1
                gui.process.listMark[index] = "Done"
            else:
                gui.process.dictionary[gui.process.listName[index]] = 0
                gui.process.listCheck[index] = 0
                gui.process.listMark[index] = "Undone"
        gui.task_due = gui.process.due_tasks()
        gui.process.save_check()
        gui.destroy_frame()
        
    def check_task(gui):
        checkTasks = []
        for tasks in gui.process.listMark:
            if tasks.lower() == "done":
                checkTasks.append(1)
            else:
                checkTasks.append(0)
        return checkTasks
    
