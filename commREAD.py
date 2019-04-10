from comSer import *
import dbProj


port3=comSer('COM3',9600)
#ctrl + k + c 
#ctrl + k + u

# while True:
#     try:
#         #float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
#         # port3.readS() is the value that is returned to serial
#         print(port3.readS())
#     except:
#         print("Keyboard Interrupt")
#         break

def checkDb():
  tvBool=True
  try:
    tvBool = dbProj.checkVal("data/test","lightShow","True")
  except:
    tvBool=True
  return tvBool

if checkDb():
    print("its true")
else:
    print("it aint")
while True:
    try:
        if dbProj.checkVal("data/python","newdata","True"):

            if dbProj.checkVal("data/python","14","1"):

                port3.lstat=False
                port3.commS()
                print("lights on")
            else:
                port3.lstat=True
                port3.commS()
                print("lights off")
            #should make receiver also contribute to a dictionary or subset of times when the value was changed
            dbProj.sendData("python","newdata",'False')
        #float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        # port3.readS() is the value that is returned to serial
        #print(port3.readS())
    except:
        print("Keyboard Interrupt")
        break