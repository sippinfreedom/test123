import yaml
import os
#import hashlib
import bcrypt
#import getpass
import pwinput

Dict = dict({})

#-------------------------------------------------------------------------------#
def checkPasswd(passwd, hashed1, check, hashed2):
    if bcrypt.checkpw(passwd, hashed1) == True and bcrypt.checkpw(check, hashed2) == True and passwd == check:
        print("Passwords Match.\nUser Registered.\nExiting SecureDrop.")
        return bytes(hashed1)
    else:
        print("Passwords do not match")
        checkP = pwinput.pwinput("Please Re-enter Password: ").encode()
        checksalt = bcrypt.gensalt()
        checkHash = bcrypt.hashpw(checkP, checksalt)
        return checkPasswd(passwd, hashed1, checkP, checkHash)      
#-------------------------------------------------------------------------------#
def createuser(salt):
    fname = input("Enter Full Name: ")
    email = input("Enter Email Address: ")

    passwd = pwinput.pwinput("Enter Password: ", mask='*').encode()
    hashed1 = bcrypt.hashpw(passwd, salt)

    check = pwinput.pwinput("Re-enter Password: ", mask='*').encode()
    salt2 = bcrypt.gensalt()
    hashed2 = bcrypt.hashpw(check, salt2)

    truePass = checkPasswd(passwd, hashed1, check, hashed2)

    user = {}
    user['Name'] = fname
    user['Email'] = email
    user['Password'] = truePass
    print(str(user["Password"]))
    #print(user)

    return user
#-------------------------------------------------------------------------------#
def checkDBEmpty(filename):
    return os.stat(filename).st_size
#-------------------------------------------------------------------------------#
def initialUserCreation():
    yn = str(input("No users are registered with this client.\nDo you want to register a new user (y/n)? "))
    if yn == "y" or yn == "Y":
        salt = bcrypt.gensalt()
        userData = createuser(salt)
        with open("ud.yaml", "w") as file:
            yaml.dump(userData, file, default_flow_style=True)
            #file.write(userData['Email'])
            #file.write(str(userData['Password']))
            file.close()
    
    elif yn == "n" or yn == "N":
        print("Exiting SecureDrop")
        exit
#-------------------------------------------------------------------------------#
def userLoginIn():
    eIn = input("Enter Email Address: ")
    verifiedEmail = False

    with open("ud.yaml") as file:
        for line in file:
            if line.strip().__contains__(eIn):
                verifiedEmail = True
                file.close()
                break
            
    pIn = input("Enter Password: ").encode()
    verifiedPassword = False
    #decrypt file

    if verifiedEmail == True and verifiedPassword == True:
        print("Welcome to SecureDrop")
        secureDrop()
    else:
        print("Email and Password Combination Invalid.")
        userLoginIn()
#-------------------------------------------------------------------------------#
def addUser():
    
    return 0
#-------------------------------------------------------------------------------#
def helpcmd():
    print("\t\"add\"  -> Add an new contact\n"
          "\t\"list\" -> List all online contacts\n"
          "\t\"send\" -> Transfer file to contact\n"
          "\t\"exit\" -> Exit SecureDrop")
    return 0

def addcmd():
    return 0

def listcmd():
    return 0

def sendcmd():
    return 0

def switch(cmd):
    match cmd:
        case "help":
            helpcmd()
        case "add":
            addcmd()
        case "list":
            listcmd()
        case "send":
            sendcmd()

#-------------------------------------------------------------------------------#
def secureDrop():
    print("Type \"help\" For Commands\n")
    cmd = input("secure_drop> ")
    while cmd != "exit":
        switch(cmd)
        cmd = input("secure_drop> ")
    print("Exiting SecureDrop")
    return 0
#-------------------------------------------------------------------------------#