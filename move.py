
import shutil
import os

source = 'C:/Users/Nicholas/Desktop/1/'
dest = 'C:/Users/Nicholas/Desktop/2/'


files = os.listdir(source)

for i in files:
    if (i.endswith(".txt")):
        shutil.move(source + i, dest)
