from cryptography.fernet import Fernet
import hashlib as hs 
import base64 as b64


class encrypter:

    def encrwithpath(key,path):
        f= Fernet(key)
        with open(path,'rb') as readbuffer:
            fileread= readbuffer.read()
        
        return f.encrypt(fileread)

    
    def encerwithdata(key,data):
        f= Fernet(key)
        return f.encrypt(data)
    



    def encerpathstore(self,key,path1,path2):
        f= Fernet(key)
        encrypted =  self.encrwithpath(key,path1)
        with open (path2, 'wb') as writebuffer:
            writebuffer.write(encrypted)




    def encerdatapathstore(key,path,data):
        f= self.encerwithdata(key,data)
        with open (path, 'wb') as writebuffer:
            writebuffer.write(encrypted)

 
    def decryptp(key,path):
        f= Fernet(key)
        with open(path,'rb') as readbuffer:
            fileread = readbuffer.read()
        return f.decrypt(fileread)



    def decrypt(key,data):
        f= Fernet(key)
        return f.decrypt(data)



    def decrypt(self,key,path1,path2):
        decrypted= self.decryptp(key,path1)
        with open (path2, 'wb') as writebuffer:
            writebuffer.write(decrypted)
    
class p2key:
    
    def Generate_key(val): 
        Key = hs.md5(val.encode()).hexdigest()
        Key = b64.urlsafe_b64encode(Key.encode())
        return Key

