import scipy.optimize as spo
import math

if __name__ == '__main__':
    b = []
    r = int(input("Ingrese el valor de R(2,3 o 4): "))
    for i in range(r):
        x = []
        for j in range(r):
            prob = float(input(f"ingrese la probabilidad de la fila {i+1}, columna {j+1}   "))
            x.append(prob)
        b.append(x)


#funcion objetivo
    def f(xy):
        c=0
        for j in range(r):
            a=0
            for i in range(r):
                a += xy[i]*b[i][j]
            if a != 0:
                c += a * math.log(1/a,2)
        e=0
        for i in range(r):
            d=0
            for j in range(r):
                if b[i][j] != 0:
                    d += b[i][j] * math.log(1/b[i][j],2)
            e += xy[i] * d
        c = c-e
        return -c

#aproximacion inicial
    xy_inicio = []
    for i in range(r):
        xy_inicio.append(1/r)

#bounds & constraints
    if r == 2:
        bnds = ((0,1),(0,1))
        cons = ({'type': 'eq', 'fun': lambda xy: xy[0]+xy[1]-1})
    if r == 3:
        bnds = ((0,1),(0,1),(0,1))
        cons = ({'type': 'eq', 'fun': lambda xy: xy[0]+xy[1]+xy[2]-1})
    if r == 4:
        bnds = ((0,1),(0,1),(0,1),(0,1))
        cons = ({'type': 'eq', 'fun': lambda xy: xy[0]+xy[1]+xy[2]+xy[3]-1})

#optimizing
    resultado = spo.minimize(f, xy_inicio, options={"disp":True}, constraints=cons, bounds=bnds)

    if resultado.success:
        print('Success')
        xy=resultado.x
        i = 0
        for item in xy:
            print(f'p(a{i+1}) = {xy[i]}')
            i += 1
    else:
        print('Fail')