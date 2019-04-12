import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
import dbProj
#from comSer import *
m=tk.Tk()
tydata=StringVar(m)
txdata=StringVar(m)
#goes with test1.ino
thBool={'key':False}

def togPress():
    dbProj.addData("imservice/messages",["message","username"],[tydata.get(),txdata.get()])
    f2.delete(0,len(tydata.get()))
    
def task():
    newM=dbProj.getBase("data/imservice/messages")
    l1['text']=""
    for thingy in newM.each():
        l1['text']=l1['text']+thingy.val()['username']+": "+thingy.val()['message']+"\n"
    
    m.after(100, task)

#port3=comSer('COM3',9600)
m.title('Messaging Service')

l2=tk.Label(text="Username:", fg="black", bg="white")
l2.pack()
f3 = tk.Entry(m,textvariable=txdata)
f3.pack()
f2 = tk.Entry(m,textvariable=tydata)
f2.pack()
button = tk.Button(m,text='send',command=togPress,width=25)
button.pack()
l1 = tk.Label(text="Messages", fg="black", bg="white")
l1.pack()
m.after(10, task)
m.mainloop()