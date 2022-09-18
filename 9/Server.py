import socket

#Haciendo uso de sockets, implemente un servidor y un cliente (a modo de ejemplo, se proveen un
#servidor y un cliente en lenguaje Python), que permita desde el cliente, enviar un archivo comprimido
#utilizando el alfabeto ABCDEFGH, y en el servidor, descomprimir el archivo.

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
CODING = {"000":"A",
          "001":"B",
          "010":"C",
          "011":"D",
          "100":"E",
          "101":"F",
          "110":"G",
          "111":"H"
}

def decode (message):
    size_msg = int(message[0])
    index_bytearray = 1
    str_byte = ""
    while index_bytearray <= len(message)-1:
        prev = bin(message[index_bytearray]).removeprefix('0b')
        if len(prev) < 8:
            prev = "0" * (8 - len(prev)) + prev
        str_byte += prev
        index_bytearray += 1
    
    i = 0
    decoded_recv = ""
    while i < size_msg * 3:
        decoded_recv += CODING[str_byte[i:i+3]]
        i += 3
    return decoded_recv

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    print (f"[*] Esperando conexiones en {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Conexion establecida con {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = decode(bytearray(data))
            print(f"Mensaje: {message}") 