from tkinter import Tk 
from tkinter.filedialog import askopenfilename
import math

def readfile(filePath:str):
    byts = []
    with open(filePath,'rb') as file:
        while True:
            byte = file.read(1)
            if not byte:
                break
            byts.append(int.from_bytes(byte, byteorder='big'))
    return byts


def calcular(byts):
    q = 256
    r = 2
    lenarchivo = len(byts)


    simbolos = []
    for ch in range(q):
        simbolos.append(ch)
    
    probabilidades = []
    for ch in simbolos:
        probabilidades.append(float(byts.count(ch)/lenarchivo))
    
    Entropia = 0
    for prob in probabilidades:
        if prob > 0:
            Entropia += prob * math.log(1/prob,r)
    print("Entropia: ", Entropia)

    EntropiaMaxima = math.log(float(q), r)

    Rendimiento = Entropia/EntropiaMaxima

    Redundancia = (1 - Rendimiento)*100
    print("Redundancia: ", Redundancia)

if __name__ == '__main__':
    
    Tk().withdraw()
    filename = askopenfilename()

    byts = readfile(filename)
    calcular(byts)