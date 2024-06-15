import tkinter as tk                 
from tkinter import ttk        
from tkinter import messagebox           
import sqlite3 as sql                    
  
# defining the function to add tasks to the list  
def add_task():  
    task_string = task_field.get()  
    # checking whether the string is empty or not  
    if len(task_string) == 0:  
        # displaying a message box with 'Empty Field' message  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        # adding the string to the tasks list  
        tasks.append(task_string) 
        the_cursor.execute('insert into tasks values (?)', (task_string ,)) 
        list_update()  
        task_field.delete(0, 'end')  
  
# defining the function to update the list  
def list_update():   
    clear_list()
    for task in tasks:  
        task_listbox.insert('end', task)  
  
# defining the function to delete a task from the list  
def delete_task():   
    try:  
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:  
            tasks.remove(the_value)    
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        # displaying the message box with 'No Item Selected' message for an exception  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# function to delete all tasks from the list  
def delete_all_tasks():  
    # displaying a message box to ask user for confirmation  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:  
        while(len(tasks) != 0):    
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  
  
# function to clear the list  
def clear_list():
    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():  
    print(tasks)  
    guiWindow.destroy()  
  
# function to retrieve data from the database  
def retrieve_database():   
    while(len(tasks) != 0):  
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  



if __name__ == "__main__":  
    guiWindow = tk.Tk()  
    guiWindow.title("TO DO LIST - Nakshita")  
    guiWindow.geometry("500x450")  
    guiWindow.resizable(0, 0)   
    guiWindow.configure( bg="#a5bfd0")

  
    the_connection = sql.connect('listOfTasks.db')  

    the_cursor = the_connection.cursor()  

    the_cursor.execute('create table if not exists tasks (title text)')  
  
  
    tasks = []  

    header_frame = tk.Frame(guiWindow, bg = "#a5bfd0")  
    functions_frame = tk.Frame(guiWindow, bg = "#a5bfd0")  
    listbox_frame = tk.Frame(guiWindow, bg = "#a5bfd0")  
  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side="right", expand=True, fill="both", pady=(0, 20), padx=(10, 10))

 
    header_label = ttk.Label(  
        header_frame,  
        text = "MY TO-DO LIST",  
        font = ("Comic Sans MS", "25", "bold", "italic"),  
        background = "#a5bfd0",  
        foreground = "#0c192c"  
    )  
    header_label.pack(padx = 20, pady = 20)  

    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Arimo", "11", "bold"),  
        background = "#a5bfd0",  
        foreground = "#000000"  
    )   
    task_label.place(x = 30, y = 40)  
      
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Arimo", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    task_field.place(x = 30, y = 80)  
  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
  

    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#a5bfd0",  
        selectforeground = "#FFFFFF"  
    ) 
    task_listbox.place(x = 10, y = 20)  
  
    retrieve_database()  
    list_update()   
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close()  
