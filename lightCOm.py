import tkinter
from tkinter import messagebox
import dbProj
#from comSer import *
m=tkinter.Tk()
#goes with test1.ino
thBool={'key':False}
def togPress():

    thBool['key']= not thBool['key'] 

    if thBool['key']==True:
        #dbProj.sendData("python","14",'1')
        dbProj.sendData("python","entireShow",'1')
        l1['text']="lights on"
    else:
        #dbProj.sendData("python","14",'0')
        dbProj.sendData("python","entireShow",'0')
        l1['text']="lights off"

def togJPress():

    thBool['key']= not thBool['key'] 

    if thBool['key']==True:
        #dbProj.sendData("python","14",'1')
        dbProj.sendData("test","lightShowJ",'Jank')
        l2['text']="jank on true"
    else:
        #dbProj.sendData("python","14",'0')
        dbProj.sendData("test","lightShowJ",'not Jank')
        l2['text']="jank off true"        
#port3=comSer('COM3',9600)
m.title('light jank on/off')
l2 = tkinter.Label(text="Jank full", fg="black", bg="white")
l2.pack()
button2 = tkinter.Button(m,text='toggle',command=togJPress,width=25)
button2.pack()
l1 = tkinter.Label(text="Test", fg="black", bg="white")
l1.pack()
button = tkinter.Button(m,text='toggle',command=togPress,width=25)

button.pack()
m.mainloop()