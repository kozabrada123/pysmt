from curses import raw
import cryptography
from cryptography.fernet import Fernet
 
import os

def makeOrLoadKey():

    if os.path.exists("./key.png"):
        key = open("./key.png")
        key = key.read().encode('ascii')
        #key = Fernet(key)
        

    else:
        key = Fernet.generate_key()
        file = open("key.png", "w")
        file.write(key.decode('ascii'))
        #print(key)
        #print(key.decode('ascii'))
        #print(key.decode('ascii').encode('ascii'))

    #Retruns bytes that can be made to stuff with Fernet()
    return key

def encryptSomething(encryption_string):
    #Encrypt a string using Fernet.
    key = makeOrLoadKey()
    f = Fernet(key)
    encrypted = f.encrypt(bytes(encryption_string, encoding='utf8'))
    return encrypted



def decryptSomething(decryption_string):
    #Encrypt a string using Fernet. (Opposite operation of encryptSomething())
    key = makeOrLoadKey()
    f = Fernet(key)
    decrypted = f.decrypt(decryption_string)
    return decrypted

def saveEncryptedCFG(username, password, email="None", emailpassword="None", mailprovider="None", emailmode="None"):


    if emailmode == "None":
        if email == "None":
            emailmode = False

        else:
            emailmode = loadEncryptedCFG()[5]


    username = encryptSomething(username)
    password = encryptSomething(password)

    if email != "None" and emailpassword != "None":
        email = encryptSomething(email)
        emailpassword = encryptSomething(emailpassword)



    #Encrypted part
    file = open("cfg.txt", "w")
    file.write(username.decode('ascii') + "\n")
    file.write(password.decode('ascii') + "\n")

    try:
        file.write(email.decode('ascii') + "\n")
        file.write(emailpassword.decode('ascii') + "\n")

    except AttributeError:
        file.write(email + "\n")
        file.write(emailpassword + "\n")

    #Unencrypted part
    file.write(mailprovider + "\n")
    file.write(str(emailmode) + "\n")
    



    file.close()

def loadEncryptedCFG():


    file = open("cfg.txt", "r")
    content = file.read()
    splitedocnt = content.splitlines()

    #When decrypting first encode it from written file and then decode to unencrypted string

    username = decryptSomething(splitedocnt[0].encode('ascii')).decode('ascii')
    password = decryptSomething(splitedocnt[1].encode('ascii')).decode('ascii')

    if splitedocnt[2] != "None" and splitedocnt[3] != "None":
        email = decryptSomething(splitedocnt[2].encode('ascii')).decode('ascii')
        emailpassword = decryptSomething(splitedocnt[3].encode('ascii')).decode('ascii')
    else:
        email = splitedocnt[2]
        emailpassword = splitedocnt[3]

    mailprovider = splitedocnt[4]
    emailmode = splitedocnt[5]

    if emailmode == "False":
        emailmode = False

    elif emailmode == "True":
        emailmode = True

    file.close()

    return username, password, email, emailpassword, mailprovider, emailmode

#Custom config loader and saver:

#cfg.txt == 
#Line 1: Active Login Username
#Line 2: Active Login Password
#Line 3: Active mail login
#Line 4: Active mail password