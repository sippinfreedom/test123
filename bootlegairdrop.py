import bcrypt
import run
from Crypto.Cipher import PKCS1_OAEP

#-------------------------------------------------------------------------------#

if run.checkDBEmpty("ud.yaml") == 0:
    run.initialUserCreation()
else:
    run.userLoginIn()

'''password = b"hmmmmmm"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print("Salt: ")
print(salt)

attempt = input("enter p: ").encode()

if bcrypt.checkpw(attempt, hashed) == True:
    print("Password Verified")
    
    
    jvasljvwlfvwififv'''
