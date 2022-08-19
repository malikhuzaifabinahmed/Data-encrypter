from tkinter import*
from tkinter import ttk
from Decrypter import Decrypter
from Encrypter import Encrypter
    


def but1():
    root.destroy()
    Encrypter()
def but2():
    root.destroy()
    Decrypter()


#Mainscreen

root = Tk()

mainframe = ttk.Frame(root,padding="130 130 130 130")
mainframe.grid(row =0 ,column =0)


Encr = ttk.Button(mainframe,text="Encrypt",width=30, command = but1 ).grid(row = 2, column= 1)

label= ttk.Label(mainframe,text="OR").grid(row=4 ,column= 1)

Encr = ttk.Button(mainframe,text="Decrypt",width=30, command = but2 ).grid(row = 6, column= 1)



root.mainloop()