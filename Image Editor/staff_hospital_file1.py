from tkinter import *
from tkinter import ttk,messagebox
import os

root=Tk()
root.title('R&A Hospital')
root.geometry('1288x900')
root.iconbitmap('Dapino-Medical-Stethoscope.ico')
bg_color="#10486C"
bg=PhotoImage('hospital.jpg')

my_label = Label(root, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

#___________variables____________
ref_var=IntVar()
dr_name_var=StringVar()
specialization_var=StringVar()
disease_var=StringVar()
bill_var=StringVar()
phone_var=StringVar()
period_var=StringVar()

#_________function______________

def add():
  if ref_var.get()==0 or dr_name_var.get()=='' or specialization_var.get()=='' or bill_var.get()=='' or disease_var.get()=='' or phone_var.get()=='' or period_var.get()=='':
    messagebox.showerror('Error','All fields are required ?')
  else:
        typearea.delete(1.0,END)
        typearea.insert(END, '\n==============================================')
        typearea.insert(END,f'\nPatient Ref\t\t\t\t{ref_var.get()}')
        typearea.insert(END, '\n==============================================')
        typearea.insert(END, f'\n\nDoctor Name\t\t\t\t{dr_name_var.get()}')
        typearea.insert(END, f'\nDisease\t\t\t\t{disease_var.get()}')
        typearea.insert(END, f'\nDoctor Specialization \t\t\t\t{specialization_var.get()}')
        typearea.insert(END, f'\nNext Checkup \t\t\t\t{period_var.get()}')
        typearea.insert(END, f'\nContact Number\t\t\t\t{phone_var.get()}')
        typearea.insert(END, f'\nTotal Bill\t\t\t\t{bill_var.get()}')
        typearea.insert(END, f'\nDiscription\t\t\t\t{discription_text.get(1.0, END)}')
        typearea.insert(END, '\n\n##################################################')

def save():
    data=typearea.get(1.0,END)
    f1=open('records project/'+str(ref_var.get())+'.txt','w')
    f1.write(data)
    f1.close()
    messagebox.showinfo('Saved',f'Ref No:{ref_var.get()} Saved Successfully')

def print():
   data=typearea.get(1.0,END)
   f='E:\\Desktop\\Python Project\\records project\\'+str(ref_var.get())+'.txt'
   os.startfile(f,'Print')

def reset():
    typearea.delete(1.0,END)
    discription_text.delete(1.0,END)
    ref_var.set(0)
    dr_name_var.set('')
    specialization_var.set('')
    period_var.set('')
    phone_var.set('')
    disease_var.set('')
    bill_var.set('')

def Exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()




# _________Heading___________
title=Label(root,text='R&A Hospital Staff',bg=bg_color,fg='white',font=('times new rommon',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)


#___________left frame details_____________

F1=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=10,y=80,width=650,height=650)

label_ref=Label(F1,text='Patient ref',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_ref.grid(row=0,column=0 , padx=30,pady=10) 

text_ref=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=ref_var)
text_ref.grid(row=0,column=1,pady=10,sticky='w')

label_dr_name=Label(F1,text='Docter Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_dr_name.grid(row=1,column=0 , padx=30,pady=10) 

text_dr_name=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=dr_name_var)
text_dr_name.grid(row=1,column=1,pady=10,sticky='w')

label_disease=Label(F1,text='Disease Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_disease.grid(row=3,column=0 , padx=30,pady=10) 

text_disease=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=disease_var)
text_disease.grid(row=3,column=1,pady=10,sticky='w')

label_specialisation=Label(F1,text='Docter Specialisation',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_specialisation.grid(row=2,column=0 , padx=30,pady=10) 

list_specialisation=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=specialization_var)
list_specialisation['value']=('General Physicians','Pediatricians','General Surgeon','Cardiologist','Dentist','Gynecologist','Ent specialist')
list_specialisation.grid(row=2,column=1,pady=10)

label_period=Label(F1,text='Next Checkup',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_period.grid(row=4,column=0 , padx=30,pady=10) 

list_des=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=period_var)
list_des['value']=('15 Days','30 Days','90 Days','180 Days','Now you are Ok')
list_des.grid(row=4,column=1,pady=10)

label_no=Label(F1,text='Contact No',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_no.grid(row=5,column=0 , padx=30,pady=10) 

text_no=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=phone_var)
text_no.grid(row=5,column=1,pady=10,sticky='w')

label_bill=Label(F1,text='Total Bill',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_bill.grid(row=6,column=0 , padx=30,pady=10) 

text_bill=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=bill_var)
text_bill.grid(row=6,column=1,pady=10,sticky='w')

label_discription=Label(F1,text='Discription',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
label_discription.grid(row=7,column=0 , padx=30,pady=10) 

discription_text=Text(F1,width=35,height=3,font=('times new rommon',10,),relief=RIDGE,bd=7)
discription_text.grid(row=7,column=1,pady=5,sticky='w')



#_________right frame details_____________
F2=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F2.place(x=665,y=80,width=650,height=650)

label_details=Label(F2,text='Doctor Prescription',font=('times new rommon',20,'bold'),fg='black',bd=7,relief=GROOVE)
label_details.pack(fill=X)

scroll=Scrollbar(F2,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
font1=['arial',15]
typearea=Text(F2,font=font1, yscrollcommand=scroll.set)
typearea.pack(fill=BOTH)
scroll.config(command=typearea.yview)

# resize

def my_fun(str1):
  if(str1=='plus'):
    font1[1]=font1[1]+2
  else:
    font1[1]=font1[1]-2
  typearea.config(font=font1)

B_zoomin=Button(root,text="+",bg='yellow',fg='red',width=2,command=lambda:my_fun('plus'))
B_zoomin.pack(anchor='e')
B_zoomin=Button(root,text="-",bg='yellow',fg='red',width=2,command=lambda:my_fun('minus'))
B_zoomin.pack(anchor='e')




#__________Buttons__________

F3=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F3.place(x=10,y=615,width=1260,height=100)


B1=Button(F3,text='Add Record',font='arial 20 bold',bg='yellow',fg='red',width=10,command=add)
B1.grid(row=0,column=0,padx=20,pady=10)

B2=Button(F3,text='Save',font='arial 20 bold',bg='yellow',fg='red',width=8,command=save)
B2.grid(row=0,column=1,padx=20,pady=10)

B3=Button(F3,text='Print',font='arial 20 bold',bg='yellow',fg='red',width=8,command=print)
B3.grid(row=0,column=2,padx=20,pady=10)

B4=Button(F3,text='Reset',font='arial 20 bold',bg='yellow',fg='red',width=8,command=reset)
B4.grid(row=0,column=3,padx=20,pady=10)

B5=Button(F3,text='Exit',font='arial 20 bold',bg='yellow',fg='red',width=8,command=Exit)
B5.grid(row=0,column=5,padx=20,pady=10)

B5=Button(F3,text='Upload',font='arial 20 bold',bg='yellow',fg='red',width=8,command=Exit)
B5.grid(row=0,column=4,padx=20,pady=10)

root.mainloop()
