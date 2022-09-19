import os
from persona import PersonaLongFija, PersonaLongVariable
import csv


def CrearDatLongFijo(lista, path):
    file = open(path+"\\DatPersonasLongFijo.dat", "w")
    for P in lista:
        file.writelines([P.Nombre, P.Direc, P.Dni, P.Primarios, P.Secundarios, P.Universitarios, P.Vivienda, P.ObraSocial, P.Trabaja, P.Soltero, P.Jubilado])
    file.close

def CrearDatLongVariable(lista, path):
    file = open(path+"\\DatPersonasLongVariable.dat", "w")
    for P in lista:
        file.write(chr(len(P.Nombre)))
        file.write(P.Nombre)
        file.write(chr(len(P.Direc)))
        file.write(P.Direc)
        file.write(P.Dni)
        file.write(chr(P.ByteBivaluado))
    file.close()


def readFileToBytes(filePath:str):
    Bytes = []
    with open(filePath,'rb') as file:
        while True:
            byte = file.read(1)
            if not byte:
                break
            Bytes.append(int.from_bytes(byte, byteorder='big'))
    return Bytes




def leercadena(inicio,fin,bytes):
    nombre = ''
    for j in range(inicio, fin):
        nombre += chr(bytes[j])
    return(nombre)

def LeerLongVariable(bytes,inicio):
    long_nom = ord(chr(bytes[inicio]))
    nombre = leercadena(inicio+1, inicio+long_nom+1,Bytes)
    long_direc = ord(chr(bytes[long_nom+1+inicio]))
    x = long_nom+2+inicio
    direc = leercadena(x, long_direc+x, Bytes)
    x = long_direc+x
    dni = leercadena(x, x+8, Bytes)
    ByteBivaluado = bytes[x+8]

    f=[]
    byteMask = 0b10000000
    for i in range(8):
            if ByteBivaluado & byteMask:
                f.append('N')
            else:
                f.append('S')
            byteMask = byteMask >> 1

    pers = PersonaLongVariable(nombre, direc, dni, f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7])
    pers.Mostrar()
    c=x+9
    return (c)



if __name__ == '__main__':
    menu=1
    while menu:
        menu = int(input("\n\nIngrese la opcion deseada: \n1: Comparar longitudes archivos .dat\n2: Recuperar datos de archivo de longitud variable\n3: Crear archivos .dat a partir de un .csv"))
        if(menu == 1):
            path = os.getcwd() + '\\DatPersonasLongVariable.dat'
            Archivo1 = len(readFileToBytes(path))

            path = os.getcwd() + '\\DatPersonasLongFijo.dat'
            Archivo2 = len(readFileToBytes(path))

            print(f'Longitud en bytes del archivo de longitud variable: {Archivo1}')
            print(f'Longitud en bytes del archivo de longitud fija: {Archivo2}')

            print(f'El Archivo de longitud fija es {Archivo2-Archivo1} bytes más largo que el Archivo de longitud variable')
        elif (menu == 2):
            path = os.getcwd() + '\\DatPersonasLongVariable.dat'
            Bytes = readFileToBytes(path)
            x=0
            for i in range(20):
                res = LeerLongVariable(Bytes,x)
                x = res
        else:
            #Cargar desde csv los .dat
            path = os.getcwd() + "\\DatosPersonas.csv"
            listaF = []
            listaV = []
            with open(path) as File:
                reader = csv.reader(File, delimiter=';')
                for f in reader:
                    listaF.append(PersonaLongFija(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10]))
                    listaV.append(PersonaLongVariable(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10]))
                File.close
            CrearDatLongVariable(listaV,os.getcwd())
            CrearDatLongFijo(listaF,os.getcwd())