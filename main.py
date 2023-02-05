
from tkinter import *
from tkinter import messagebox

import mysql.connector



root=Tk()
root.configure(background='light green')
root.title("Registration Form")
root.geometry("400x400")
root.resizable(False,False)
#method
def clear():
  name_entry.delete(0, END)
  age_entry.delete(0,END)
  phone_entry.delete(0,END)
  email_entry.delete(0,END)

def register():
    name=name_info.get()
    age=age_info.get()
    phone=phone_info.get()
    email=email_info.get()

    if name=="":
        messagebox.showerror("Error","Please enter your name")
    elif age=="":
        messagebox.showerror("Error", "Please enter your age")
    elif phone=="":
        messagebox.showerror("Error", "Please enter your phone")
    elif email=="":
        messagebox.showerror("Error", "Please enter your email")
    else:
        con=mysql.connector.connect(host="localhost",user="root",password="",database="form")
        cursor=con.cursor()
        cursor.execute("insert into first values('"+name+"','"+age+"','"+phone+"','"+email+"')")
        cursor.execute("commit");
        messagebox.showinfo("status","Registration Successful");
        con.close();
    clear()
        #Label(root,text="Registration Successful",font="20",fg="green").place(x=135,y=285)





#form internal part
Label(root,text="Registration Form",font="ariel 20 bold",bg="yellow").pack(fill="both")

Label(root,text="Name",font="20").place(x=40,y=75)
Label(root,text="Age",font="20").place(x=40,y=115)
Label(root,text="Phone",font="20").place(x=40,y=155)
Label(root,text="Email",font="20").place(x=40,y=195)
#variable
name_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()
#entry
name_entry=Entry(root,font="10",bd=4,textvariable=name_info)
name_entry.place(x=140,y=75)
age_entry=Entry(root,font="10",bd=4,textvariable=age_info)
age_entry.place(x=140,y=115)
phone_entry=Entry(root,font="10",bd=4,textvariable=phone_info)
phone_entry.place(x=140,y=155)
email_entry=Entry(root,font="10",bd=4,textvariable=email_info)
email_entry.place(x=140,y=195)

Button(root,text="Register",bg="black",fg="white",font="20",command=register).place(x=185,y=255)
clear()


mainloop()