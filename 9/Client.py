import socket
import re

#Haciendo uso de sockets, implemente un servidor y un cliente (a modo de ejemplo, se proveen un
#servidor y un cliente en lenguaje Python), que permita desde el cliente, enviar un archivo comprimido
#utilizando el alfabeto ABCDEFGH, y en el servidor, descomprimir el archivo.

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
CODING = {"A":int('000',2),
          "B":int("001",2),
          "C":int("010",2),
          "D":int("011",2),
          "E":int("100",2),
          "F":int("101",2),
          "G":int("110",2),
          "H":int("111",2)
}

def encode (message):
    if re.fullmatch('[ABCDEFGH]+', message) != None:
        num_of_bytes = int((len(message)/3)+1)
        encoding_to_send = bytearray(num_of_bytes+1)
        encoding_to_send[0] = int(bin(len(message)),2) #Agrego un byte con la cantidad de caracteres
        index_bytearray = 1
        curr_bits = 8
        end_of_byte = 3
        for i, char in enumerate(message):
            if end_of_byte == 3:
                if curr_bits >= 3: #todavia se pueden agregar letras al byte
                    encoding_to_send[index_bytearray] = encoding_to_send[index_bytearray] | CODING[char]<<curr_bits - end_of_byte
                else: #Se alcanzó el limite del byte
                    if curr_bits == 1: #Queda 1 bit del byte para usarse
                        byte = (int('00000000',2) | CODING[char]>>2) <<2
                    elif curr_bits == 2: #Quedan 2 bits del byte para usarse
                        byte = (int('00000000',2) | CODING[char]>>1) <<1
                    byte_aux = CODING[char] - byte
                    end_of_byte = 3 - curr_bits
                    encoding_to_send[index_bytearray] = encoding_to_send[index_bytearray] | CODING[char]>>end_of_byte
                    curr_bits = curr_bits - 3
                curr_bits = curr_bits - end_of_byte
            if curr_bits < 0:
                index_bytearray += 1
                curr_bits = 8
                encoding_to_send[index_bytearray] = encoding_to_send[index_bytearray] | byte_aux<<curr_bits-end_of_byte #Agrego los bits que quedaron del último caracter
                curr_bits = curr_bits - end_of_byte
                end_of_byte = 3
    else:
        print("Ese no es nuestro alfabeto")
        encoding_to_send = "error"
    return encoding_to_send

with socket.socket() as s:
    s.connect((HOST, PORT))
    message = input("Ingrese el mensaje a enviar: ")
    while message != "":
        message = encode(message)
        if message == "error":
            break
        print(f"vamos a enviar: {message}")
        s.send(message)
        message = input("Ingrese el mensaje a enviar: ")