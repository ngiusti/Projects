import tkinter
from tkinter import filedialog
from tkinter import *
import checkmod
import os
import time
import shutil

#global variables
source_path = []
destination_path = []
#display messages on the buttons
srcText ='Select Source Directory'
destText = 'Select Destination Directory'
executeText = "Files Transfered"
#the source point for the files to be moved.
def srcDir():
    srcName = filedialog.askdirectory()
    srcBut["text"]= str(srcName) if srcName else srcText
    source = srcName + "/"
    source_path.append(source)
    print (source)
    
#the destination point for the files to be moved.
def destDir():
    destName = filedialog.askdirectory()
    destBut["text"] = str(destName) if destName else destText
    destination = destName + "/"
    destination_path.append(destination)
    print (destination)
    
#The execute action for the file transfer
def execute():
    checkMod()
    executeBut["text"] = str(executeText) if execute else executeText

#The function for checking the time since the files have been
#edited/created then moving them.
def checkMod():
    
    source = source_path[0]
    dest = destination_path[0]  
    past = (time.time() - 24*60*60)
    files = os.listdir(source)
    for i in files:
        if time.ctime(os.path.getmtime(source + i)) >= time.ctime(past): # added + i to identify the folder. 
            shutil.move(source + i, dest)
            print ("Files have been transfered")
        else:
            print ("Not a new file")


if __name__ == '__main__':
    root = Tk()
root.title('File Transfer')

#Buttons for the box
button_opt = {'fill': constants.BOTH, 'padx': 5, 'pady': 5}


srcBut = Button(root, text = srcText, fg = 'black', command = srcDir)
srcBut.grid(row = 0, column = 1, sticky = N+E+W+S)

destBut = Button(root, text = destText, fg = 'black', command = destDir)
destBut.grid(row = 2, column = 1, sticky = N+E+W+S)

executeBut = Button(root, text = "Execute", fg = 'black', command = execute)
executeBut.grid(row = 4, column = 1, sticky = N+E+W+S)


slbl = Label(text = "Source:  ", bg = "#E1CEC1", fg = "black")
slbl.grid(row = 0, column = 0, sticky = W)
dlbl = Label(text = "Destination:  ", bg = "#E1CEC1 ", fg = "black")
dlbl.grid(row = 2, column = 0, sticky = W)
elbl = Label(text = "Execute:  ", bg = "#E1CEC1", fg = "black")
elbl.grid(row = 4, column = 0, sticky = W)

root.configure(bg = "#E1CEC1")


root.mainloop()
