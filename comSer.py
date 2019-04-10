import serial
class comSer:
    def __init__(self,cPort,cRate):
        self.lstat=False
        self.ser = serial.Serial(cPort,cRate)

    def commS(self):
        if self.lstat:
            self.ser.write('0'.encode())
            self.lstat=False
        elif not self.lstat:
            self.ser.write('1'.encode())
            self.lstat=True
        #l1['text']=readS() 

    def readS(self):
        self.ser_bytes = self.ser.readline()
        self.dser_bytes =self.ser_bytes[0:len(self.ser_bytes)-2].decode("utf-8")
        return self.dser_bytes
    def writeS(self,ttext):
        self.ser.write(ttext.encode())