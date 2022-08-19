from cryptography.fernet import Fernet
from utils import p2key 
from utils import encrypter as Enc 
import os 



def encrypter(password,targetdirpath):
   
    Key= p2key.Generate_key(password)
    

    listdir=os.listdir(targetdirpath)
    
    for item in listdir:
        splitname = os.path.splitext(item)
        Enc.encerpathstore(Enc,Key,os.path.join(targetdirpath, item),os.path.join(targetdirpath, item))



def decrypter(password,targetdirpath):
    Key= p2key.Generate_key(password)
    listdir=os.listdir(targetdirpath)

    try:

        
        
        for item in listdir:
            splitname = os.path.splitext(item)
            path= os.path.join(targetdirpath, item)
            Enc.decrypt(Enc,Key,path,path)
    except ValueError:
        return ValueError
        pass

