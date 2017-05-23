import os
import time
import shutil
# this is stating the 24 hour period 
past = (time.time() - 24*60*60)
print past

source = 'C:/Users/Nicholas/Desktop/2/'
dest = 'C:/Users/Nicholas/Desktop/1/'


files = os.listdir(source)

for i in files:
    if time.ctime(os.path.getmtime(source + i)) >= time.ctime(past): # added + i to identify the folder. 
        shutil.move(source + i, dest)
        print ("Files have been transfered")
    else:
        print ("Nothing New")
