
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
import os
from encer import encrypter
def Encrypter():
     



    def Create(*args):
        try:
            if (passa.get()!='' and passb.get()!= '' and filepath.get() !=  '' ):
                if (passa.get()==passb.get()):
                    if(os.path.exists(filepath.get())):
                        encrypter(passa.get(),filepath.get())
                        result.set('Done')
                    else:
                        result.set('Enter a valid Path')  
                else:
                    result.set('Password Dont match')  
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
    root.title("Create New Wallet")

    mainframe = ttk.Frame(root, padding="12 12 12 12")
    mainframe.grid(column=0, row=0 )
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=4)
    #browse

    filepath = StringVar()
    ttk.Label(mainframe, text="Enter the path to save Wallet",).grid(column=2, row=2)
    ttk.Entry(mainframe, width=7, textvariable=filepath).grid(column=3, row=2,columnspan= 200,sticky=(W, E))
    ttk.Button(mainframe, text="Browse", command=browse).grid(column=220, row=2, sticky=W)

    #passwordEntry
    ttk.Label(mainframe, text="Password").grid(column=2, row=4)
    passa = StringVar()
    passa_entry = ttk.Entry(mainframe, width=80, textvariable=passa ,show = "*")
    passa_entry.grid(column=3, row=4,columnspan= 200, sticky=(W, E))

    #confirm password entry
    ttk.Label(mainframe, text="Confirm Password").grid(column=2, row=6)
    passb = StringVar()
    passb_entry = ttk.Entry(mainframe, width=7, textvariable=passb,show = "*")
    passb_entry.grid(column=3, row=6, columnspan= 200,sticky=(W, E))

    #result
    result = StringVar()
    ttk.Label(mainframe, textvariable=result).grid(column=3, row=8)




    #button Entry

    ttk.Button(mainframe, text="Encrypt", command=Create,width=40).grid(column=2, row=12, sticky=W)
    

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
