from tkinter import*
from tkinter import ttk
from tkinter import filedialog
import os

from encer import decrypter

def Decrypter():
    def compare(*args):
        try:
            if (passa.get()!='' and filepath.get() !=  '' ):
                    
                    if(os.path.exists(filepath.get())):
                        #Call DEcrypting Function
                        value= decrypter(passa.get(),filepath.get())
                        if (value!= 'None'):
                            result.set(value)
                        else:
                            result.set('Done')
                    else:
                        result.set('Enter a valid Path')  
            else:
                result.set('All fields Must be filled')

        except ValueError:
            pass
       
    def browse(*args):
        try:
            file = filedialog.askdirectory(parent=root,title='Choose a file')
            filepath.set(file)
        except ValueError:
            pass

    

    root = Tk()

    root.title("Sign in of Wallet")
    mainframe = ttk.Frame(root,padding= "20 20 20 20")
    mainframe.grid(column=0, row=0 )
    root.columnconfigure(0, weight=1)
    root.rowconfigure(2, weight=4)
    #passwordEntry
    ttk.Label(mainframe, text="Password").grid(column=2, row=2)
    passa = StringVar()
    passa_entry = ttk.Entry(mainframe, width=80, textvariable=passa,show="*")
    passa_entry.grid(column=3, row=2,columnspan= 200, sticky=(W, E))

    #empty label


    # for i in range(4,7):
    #     ttk.Label(mainframe,text= "").grid(column=2,row=i )

    #browse

    filepath = StringVar()
    ttk.Label(mainframe, text="Enter the path to save Wallet",).grid(column=2, row=8)
    ttk.Entry(mainframe, width=7, textvariable=filepath).grid(column=3, row=8,columnspan= 200,sticky=(W, E))
    ttk.Button(mainframe, text="Browse", command=browse).grid(column=220, row=8, sticky=W)
    #result
    result = StringVar()
    ttk.Label(mainframe, textvariable=result).grid(column=3, row=10)

    #button

    ttk.Button(mainframe, text="Decrypt", command=compare,width=40).grid(column=2, row=12, sticky=W)
    

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

