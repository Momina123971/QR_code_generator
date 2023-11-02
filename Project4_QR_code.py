#First going to import a module for qrcode.
import pyqrcode
#making qrcode of my name.
name="Momina Mehboob"
#making an object.
k=pyqrcode.create(name)
#scale define the size of qrcode.
k.png("test.png",scale=2)

#importing a os module which interact with our operating system.
import os
#it will open the file of our qrcode.
os.system("test.png")


