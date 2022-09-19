
class PersonaLongFija:
    def __init__(self, nombre, direc, dni, primarios, secundarios, universitarios,
                 vivienda, obraSocial, trabaja, soltero, jubilado):
        if len(nombre) < 40:
            self.Nombre = nombre + (" "*(40-len(nombre)))
        else:
            self.Mombre = nombre[:40]

        if len(direc) < 40:
            self.Direc = direc + (" "*(40-len(direc)))
        else:
            self.Direc = direc[:40]

        self.Dni = dni[:8]

        self.Primarios = primarios
        self.Secundarios = secundarios
        self.Universitarios = universitarios
        self.Vivienda = vivienda
        self.ObraSocial = obraSocial
        self.Trabaja = trabaja
        self.Soltero = soltero
        self.Jubilado = jubilado



    def Mostrar(self):
        print(f"Apellido y Nombre: {self.Nombre}\n")
        print(f"Dirección: {self.Direc}\n")
        print(f"DNI: {self.Dni}")
        print(f"Estudios Primarios: {self.Primarios}")
        print(f"Estudios Secundarios: {self.Secundarios}")
        print(f"Estudios Universitarios: {self.Universitarios}")
        print(f"Tiene vivienda: {self.Vivienda}")
        print(f"Tiene Obra Social: {self.ObraSocial}")
        print(f"Trabaja: {self.Trabaja}")
        print(f"Es soltero:{self.Soltero}")
        print(f"Es jubilado: {self.Jubilado}")


class PersonaLongVariable:
    def __init__(self, nombre, direc, dni, primarios, secundarios, universitarios,
                 vivienda, obraSocial, trabaja, soltero, jubilado):
        self.Nombre = nombre
        self.Direc = direc
        self.Dni = dni[:8]
        self.ByteBivaluado = self.Bivaluado(primarios, secundarios, universitarios,
                                            vivienda, obraSocial, trabaja, 
                                            soltero, jubilado)

    def Mostrar(self):
        print(f"Apellido y Nombre: {self.Nombre}")
        print(f"Dirección: {self.Direc}")
        print(f"DNI: {self.Dni}")
        byteMask = 0b10000000
        for i in range(8):
            if self.ByteBivaluado & byteMask == 0:
                print(f"Campo {i+1}: Si")
            else:
                print(f"Campo {i+1}: No")
            byteMask = byteMask >> 1

    def Bivaluado(self, p, s, u, v, os, t, sol, j):
        byte = int('00000000',2)
        if p == 'S':
            byte = byte | 0b10000000
        if s == 'S':
            byte = byte | 0b1000000
        if u == 'S':
            byte = byte | 0b100000
        if v == 'S':
            byte = byte | 0b10000
        if os == 'S':
            byte = byte | 0b1000
        if t == 'S':
            byte = byte | 0b100
        if sol == 'S':
            byte = byte | 0b10
        if j == 'S':
            byte = byte | 0b1
        return byte



