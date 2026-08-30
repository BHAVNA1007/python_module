'''
"Tkinter is part of Python's standard library and is used to create GUI applications. It usually comes bundled with the standard Python installation."

'''




import tkinter as tk

root = tk.Tk()   #Creates the main/root window.

root.title('Module learning...')  #Sets the window title.

root.geometry('500x500') 

label = tk.Label(root, text="learning tkinter")
label.pack()

label = tk.Label(root, text="ENTER YOUR NAME")
label.pack()


entry = tk.Entry(root)
entry.pack()


def submit():
   name = entry.get()
   print(name)


button = tk.Button(root, text="Submit",  command = submit)
button.pack()

'''
tk.Label → creates a label
root → puts the label inside the main window
text= → text displayed on the label
'''

#root.resizable(False, False)
root.mainloop() #Starts the event loop, which keeps the GUI running and handles user events.

