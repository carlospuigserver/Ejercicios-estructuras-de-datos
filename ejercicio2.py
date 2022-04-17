from asyncore import write


class usuario:
    def __init__(self,linea1,linea2):
        self.linea1=linea1
        self.linea2=linea2
        #mayúsculas
        linea1.upper()
        linea2.upper()

def fichero(self):
    archivo=open("xxxx.txt","w")
    archivo.write(self.linea1)
    archivo.write(self.linea2)
    archivo.close()
