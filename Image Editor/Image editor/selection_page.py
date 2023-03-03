from email import message
from PIL import ImageTk, Image
from tkinter import *

sel_scr=Tk()
sel_scr.title("Select Role")
sel_scr.geometry("800x600")
message = "Select your fucking occupation"

def nextPage():
    sel_scr.destroy()
    import login_page


Label(sel_scr, text="Choose Your Role").grid(row=0,column=6)

Button(sel_scr, text="Doctor", width=20, height=2, bg="#3F72AF",command=nextPage).grid(row=2,column=5)
Button(sel_scr, text="Staff", width=20, height=2, bg="#3F72AF",command=nextPage).grid(row=2,column=6)
Button(sel_scr, text="Patient", width=20, height=2, bg="#3F72AF",command=nextPage).grid(row=2,column=7)

canvas2 = Canvas(sel_scr, width = 300, height = 300)      
canvas2.grid(row=4,column=5)      
img2 = PhotoImage(file="doctor.png")      
canvas2.create_image(20,20, anchor=NW, image=img2) 

canvas = Canvas(sel_scr, width = 300, height = 300)      
canvas.grid(row=4,column=7)      
img = PhotoImage(file="patient.png")      
canvas.create_image(20,20, anchor=NW, image=img) 

canvas3 = Canvas(sel_scr, width = 300, height = 300)      
canvas3.grid(row=4,column=6)      
img3 = PhotoImage(file="nurse.png")      
canvas3.create_image(20,20, anchor=NW, image=img3) 


mainloop()