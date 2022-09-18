#Referencias Levenshtein
#            https://jairoandres.com/string-matching-a-lo-pythonico/
#            https://medium.com/@diego.campos.sobrino/m%C3%A9tricas-de-similitud-para-cadenas-de-texto-parte-iv-biblioteca-hermetrics-para-python-33404f0ddb70

#Desarrollar un programa para comparar dos cadenas, no en forma tradicional (carácter por carácter), sino
#que implemente un algoritmo, propuesto por Ud., que determine el parecido, por ejemplo de cadenas como:
#Juan Perez y Jaun Perez, Horacio López y Oracio López, cadenas que si se tratan en comparando carácter por
#carácter, son muy poco parecidas o incluso no se parecen en nada.

def CompararCadenas(cadena1, cadena2):
    if cadena1 == cadena2:
        return True

    resultado = 0                                           #Este algoritmo se basa en ver si el caracter se encuentra en la otra cadena a una distancia 1 de su posición original
    if len(cadena1) <= len(cadena2):                        #Contabiliza los aciertos y si supera un 70 % de aciertos, cuenta como si las cadenas fueran similares por lo que envia un True
        for i, ch in enumerate(cadena1):
            if i == 0:
                if ch == cadena2[0] or ch == cadena2[1]:
                    resultado += 1
            elif i == (len(cadena1)-1):
                if len(cadena1) == len(cadena2):
                    if ch == cadena2[i] or ch == cadena2[i-1]:
                        resultado += 1
                else:
                    if ch == cadena2[i] or ch == cadena2[i-1] or ch == cadena2[i+1]:
                        resultado += 1
            else:
                if ch == cadena2[i] or ch == cadena2[i-1] or ch == cadena2[i+1]:
                    resultado += 1
    else:
        if len(cadena2) > 0:
            for i, ch in enumerate(cadena1):            
                if i == 0:
                    if ch == cadena2[0]:
                        resultado += 1
                    elif len(cadena2) > 1 and ch == cadena2[1]:
                        resultado += 1
                elif i < len(cadena2)-1:
                    if ch == cadena2[i] or ch == cadena2[i-1] or ch == cadena2[i+1]:
                        resultado += 1
                elif i == len(cadena2)-1:
                    if ch == cadena2[i] or ch == cadena2[i-1]:
                        resultado += 1
                else:
                    break
        else:
            print("segunda cadena vacia")
    rv = (resultado * 100) / len(cadena1)
    return rv > 70

"""
    cadena1 = cadena1.lower()
    cadena2 = cadena1.lower()
    if cadena1[0] == "h":                       #En el Idioma ESPAÑOL, si una palabra comienza con H, esta nunca emitirá sonido al pronunciarce
        cadena1= cadena1.replace("h", "")       # por ello es que la eliminamos de la comparación 🤙​
    if cadena2[0] == "h":
        cadena2= cadena2.replace("h", "")

    if len(cadena1) == len(cadena2) and cadena1[0] == cadena2[0] and cadena1[-1] == cadena2[-1]: #El algoritmo se basa en un estudio de una Universidad Inglesa
        return True
    else:
        return False       
"""        
"""
    resultado = 0                                   #Algoritmo qe se basa en un sistema hipotético de puntos donde si las cadenas tienen el mismo largo suma punto
    if len(cadena1) == len(cadena2):                #Si contiene los mismos caracteres, suma más puntos
        resultado += 1                              #Si la posicion de los caracteres es la misma en ambas cadenas, suma más puntos
                                                    #A mayor puntaje, más parecidas serán las cadenas
    A = cadena1.split()
    B = cadena2.split()
    for i in A:
        for j in B:
            if sorted(i) == sorted(j):
                resultado += 1

    for i, ch1 in enumerate(cadena1):
        for j, ch2 in enumerate(cadena2):
            if i == j and ch1 == ch2:
                resultado += 1

    return resultado            
""" 

print(CompararCadenas("Horacio López", "Oracio López,"))