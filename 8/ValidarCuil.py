#Referencia https://maurobernal.com.ar/cuil/calcular-el-cuil/

#Implementar un programa que valide un CUIT/CUIL ingresado por teclado.

def validarCUITCUIL(cuit):
    if (not cuit): 
        raise Exception("CUIT/CUIL invalido")
    if (len(cuit) != 13):  
        raise Exception("CUIT/CUIL incorrecto")
    if (cuit[2] != "-" and cuit[11] != "-"):
        raise Exception("CUIT/CUIL incorreto")
    rv = False
    resultado = 0
    cuit_nro = cuit.replace("-", "")
    codes = "6789456789"
    cuit_long = int(cuit_nro)
    verificador = int(cuit_nro[len(cuit_nro)-1]) 
    
    x = 0
    while x < 10:
        digitoValidador = codes[x]
        digito = cuit_nro[x]
        if digitoValidador and digito:
            digitoValidacion = int(digitoValidador) * int(digito)
            resultado += digitoValidacion
        x = x + 1
    resultado = resultado % 11
    rv = (resultado == verificador)
    return rv

print(validarCUITCUIL(input("Ingerese el CUIL a validad:")))