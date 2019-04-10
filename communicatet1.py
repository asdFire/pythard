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
        dbProj.sendData("python","14",'1')
        dbProj.sendData("python","newdata",'True')
        l1['text']="1"
    else:
        dbProj.sendData("python","14",'0')
        dbProj.sendData("python","newdata",'True')
        l1['text']="0"
        
#port3=comSer('COM3',9600)
m.title('Serial on/off')
l1 = tkinter.Label(text="Test", fg="black", bg="white")
l1.pack()
button = tkinter.Button(m,text='toggle',command=togPress,width=25)

button.pack()
m.mainloop()