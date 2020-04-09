from tkinter import * 
import sqlite3 
 
root = Tk() 
root.geometry('500x500') 
root.title("Registration Form") 
 
Fullname=StringVar() 
Email=StringVar() 
var = IntVar() 
c=StringVar() 
var1= IntVar() 
def close_window():
    root.destroy() 
 
def database():    
    name1=Fullname.get()    
    email=Email.get()    
    gender=var.get()    
    country=c.get()    
    hobby=var1.get()    
    conn = sqlite3.connect('Registration Form.db')    
    with conn: 
      cursor=conn.cursor()    
      cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Hobby TEXT)')    
      cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Hobby) VALUES(?,?,?,?,?)',(name1,email,gender,country,hobby,))    
      conn.commit()                       
      
label_0 = Label(root, text="Registration form",width=20,font=("bold", 30)) 
label_0.place(x=30,y=53) 
 
label_1 = Label(root, text="FullName :",width=20,font=("bold", 15)) 
label_1.place(x=38,y=130) 
 
entry_1 = Entry(root,textvar=Fullname) 
entry_1.place(x=240,y=130) 
 
label_2 = Label(root, text="Email :",width=20,font=("bold", 15)) 
label_2.place(x=53,y=180) 
 
entry_2 = Entry(root,textvar=Email) 
entry_2.place(x=240,y=180) 
 
label_3 = Label(root, text="Gender :",width=20,font=("bold", 15)) 
label_3.place(x=43,y=230) 
 
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230) 
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230) 
 
label_4 = Label(root, text="State :",width=20,font=("bold", 15)) 
label_4.place(x=53,y=280) 
 
list1 = ['New Delhi','Punjab','Haryana','Himatchal Pardesh','Uttrakhand','Mumbai']; 
 
droplist=OptionMenu(root,c, *list1) 
droplist.config(width=15) 
c.set('select your country')  
droplist.place(x=240,y=280) 
 
label_4 = Label(root, text="Hobby :",width=20,font=("bold", 15)) 
label_4.place(x=48,y=330) 
var2= IntVar() 
Checkbutton(root, text="Indoor games", variable=var1).place(x=225,y=330) 
 
Checkbutton(root, text="Outdoor games", variable=var2).place(x=330,y=330) 
 
Button(root, text='Submit',width=20,bg='green',fg='white',command=database).place(x=100,y=380) 
Button(root, text='Exit',width=20,bg='green',fg='white',command=close_window).place(x=270,y=380) 
 
root.mainloop()
