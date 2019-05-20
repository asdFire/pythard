import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
import dbProj
#from comSer import *
m=tk.Tk()
tydata=StringVar(m)
txdata=StringVar(m)
#goes with test1.ino
pUsername=""
loggedIn={'key':False}


def togPress(event=None):
    '''Send message after return or button is pressed'''
    if loggedIn['key']==False:
        login()
    if not tydata.get()=='' and not tydata.get()=='clearMessage':
        dbProj.addData("imservice/messages",["message","username"],[tydata.get(),txdata.get()])
        print("\'"+tydata.get()+"\'")
    elif tydata.get()=='clearMessage':
        clearMessage()
    f2.delete(0,len(tydata.get()))
    f2.focus_set()

def task():
    '''check database for messages'''
    #figure out sometime why dictionaries are always global but a variable isnt
    if loggedIn['key']:
        #print("hey")
        newM=dbProj.getBase("data/imservice/messages")
        l1['text']=""
        for thingy in newM.each():
            l1['text']=l1['text']+thingy.val()['username']+": "+thingy.val()['message']+"\n"


    m.after(100, task)
def clearMessage():
    dbProj.db.child('data/imservice/messages').remove()
    dbProj.db.child('data/imservice/messages').push({"username":':',"message":':'})

def login():
    '''set username so that it disapears'''
    if not txdata.get().strip()=='':
        l2.pack_forget()
        f3.pack_forget()
        buttonl.pack_forget()
        #if this crap is a regular boolean variable it saves as local
        loggedIn['key']=True
        print("loggedIn is true")
        f2.pack()
        button.pack()
        l1.pack()
        f2.focus_set()

#port3=comSer('COM3',9600)
m.title('Messaging Service')
m.bind('<Return>', togPress)

l2=tk.Label(text="Username:", fg="black", bg="white")
l2.pack()
f3 = tk.Entry(m,textvariable=txdata)
f3.pack()
buttonl = tk.Button(m,text='login',command=login,width=25)
buttonl.pack()

f2 = tk.Entry(m,textvariable=tydata)

button = tk.Button(m,text='send',command=togPress,width=25)

l1 = tk.Label(text="", fg="black", bg="white")

m.after(10, task)
m.mainloop()
