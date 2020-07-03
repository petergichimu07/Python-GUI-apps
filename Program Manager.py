import tkinter as tk

from tkinter import filedialog, Text
from  tkinter import messagebox as msg
import os

root = tk.Tk()
root.title('Program Manager')
root.resizable(0,0)

apps = []
selected = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#this manages the display


# this function tells the app what to do when the button is pressed
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/",title = "Select file",
                                          filetypes =(("executables",".exe"),("all files","*.*")))
    apps.append(filename)

    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')
    displayMaster()





#this creates a canvas(window) for displaying stuff
canvas =tk.Canvas(root,height=500,width=500, bg= "#263D42",)
canvas.pack(fill ="y")



#this is a frame within the window
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.7,relheight=0.7,relx=0.1,rely=0.1)

information = tk.Label(frame, text="Apps You Like", bg = "green", fg= "white",padx=150,pady=4)
information.pack()

#this creates the button labeled add app
openFile=tk.Button(root, text = "Add App",padx =10,
                   pady=5, fg="white",bg="#263D42", command=addApp)
openFile.pack()

#this function runs the applications selected
def runMe():
    for app in apps:


        os.startfile(app)
#this function runs the display, it shows the selected applications
def displayMaster():


   for app in apps:
       information = tk.Label(frame, text=app, fg="black")
       
       information.pack()


displayMaster()

#this is the button for running the applications
runApps = tk.Button(frame,text = "Run Apps", bg = "#263d43", fg="white", command = runMe )
runApps.pack()










root.mainloop()

