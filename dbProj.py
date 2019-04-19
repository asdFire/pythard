import pyrebase
config = {
  "apiKey": "AIzaSyCwJJHvNPqeVDPNSVVH6I91MeSFHbmfKqQ",
  "authDomain": "testproject-2935a.firebaseapp.com",
  "databaseURL": "https://testproject-2935a.firebaseio.com",
  "storageBucket": "testproject-2935a.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#actually get dictionary at tpath but whatever
def checkBase(tpath):
  tbasechk=db.child(tpath).get()
  return tbasechk.val()

def getBase(tpath):
  tbasechk=db.child(tpath).get()
  return tbasechk
def sendData(tpath,tkey,tval):
  #we need to check first
  ldata = {}
  #see line 21
  ldata=checkBase("data/"+tpath)
  if ldata is None:
    ldata={}
  #this should work as is
  ldata[tkey]=tval
  #ldata.update({txdata.get():tydata.get()})
  #ldata={txdata.get():tydata.get()}
  #need to make this an update upon read if there
  db.child("data/"+tpath).set(ldata)
  #messagebox.showinfo("Sending data","sent")

def addData(tpath,tkey,tval):
  ldata = {}
  # #see line 21
  # ldata=checkBase("data/"+tpath)
  # if ldata is None:
  #   ldata={}
  #this should work as is

  #turn this into a tkey.length thing in a try statement later
  try:
    ldata[tkey[0]]=tval[0]
    ldata[tkey[1]]=tval[1]
    ldata[tkey[2]]=tval[2]
  except:
    print("huhh")
  try:
    ldata[tkey]=tval
  except:
    print("huh")

  #ldata.update({txdata.get():tydata.get()})
  #ldata={txdata.get():tydata.get()}
  #need to make this an update upon read if there
  db.child("data/"+tpath).push(ldata)

def getData(tpath):
  ldata=checkBase(tpath)

  if ldata is None:
    ldata={}
  return ldata

def checkVal(tpath,tkey,chkVal):
  ldata = getData(tpath)
  tBool=False
  if ldata[tkey]==chkVal:
    tBool=True

  return tBool
