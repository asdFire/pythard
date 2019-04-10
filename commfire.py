import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
import dbProj


m=tk.Tk()
m.title("firebase data storing")
m.geometry("400x146")
m.resizable(1, 0)



#data for value
tydata=StringVar(m)
#data for key
txdata=StringVar(m)
#data for unique tag/path
tcdata=StringVar(m)



def sendDatab():
  dbProj.sendData(tcdata.get(),txdata.get(),tydata.get())
  

w = tk.Label(m, text="unique tag:")
w.pack()
f2 = tk.Entry(m,textvariable=tcdata)
f2.pack()
w2 = tk.Label(m, text="key:")
w2.pack()
f = tk.Entry(m,textvariable=txdata)
f.pack()
w2 = tk.Label(m, text="val:")
w2.pack()
e = tk.Entry(m,textvariable=tydata)
e.pack()
b1=tk.Button(m,text='Send',command=sendDatab,width=25)
b1.pack()

#b2=tk.Button(m,text='Search',command=  ,width=25)
#b2.pack()
m.mainloop()

