# Checking file is empty or not 

import os 
size= os.stat("testfile.txt").st_size

if size==0:
	print("The file is empty")
else:
	print("The file is not empty")