from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from tkinter import PhotoImage

GUI = Tk()
GUI.title('เมนูอาหาร')
GUI.geometry('500x400')

L1 = Label(GUI,text='เมนูอาหารร้านนี้',font=('Angsana New',30),fg='green')
L1.place (x=30,y=20)

def Button1():
    text = '- กระเพาะ\n - ข้าวผัด\n - ราดหน้า'
    messagebox.showinfo('เมนูอาหาร',text)

FB1 = LabelFrame(GUI)
FB1.place(x=100,y=80)

B1 = ttk.Button(FB1,text='เมนูอาหาร',command=Button1)
B1.pack(ipadx=28,ipady=20)

def Button2():
    text = '- บัวลอย\n - ลอดช่อง\n - เฉาก๋วย'
    messagebox.showinfo('เมนูของหวาน',text)

FB2 = LabelFrame(GUI)
FB2.place(x=100,y=180)

B2 = ttk.Button(FB2,text='เมนูของหวาน',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = '- ชานม\n - กาแฟ\n - น้ำเปล่า'
    messagebox.showinfo('เมนูเครื่องดื่ม',text)

FB3 = LabelFrame(GUI)
FB3.place(x=100,y=280)

B3 = ttk.Button(FB3,text='เมนูเครื่องดื่ม',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
