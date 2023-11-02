#First going to import a module for qrcode.
import pyqrcode
#making qrcode of my name.
name="https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHFyYi1sSlFQU2p3UGJ1Ml9CN0tnQ0pGWFU1UXxBQ3Jtc0ttWS1EcW42cjVDZDZ5TS1kckFYSU1KOXRnd25Eb3F1Y21DQ1JQeUFXdHR1MU5qMWdPQjB3Y2tlcVhzMXlBeWNRTWZsaEFTVk9tYnF4blJ1LUNuRFp0bml5VUxKUEI0QzBMYUFQOXNjSEtaTVFSRkVyWQ&q=https%3A%2F%2Fgithub.com%2Ftechwithtim%2F3-Python-Automation-Projects&v=Oz3W-LKfafE"
#making an object.
k=pyqrcode.create(name)
#scale define the size of qrcode.
k.png("test.png",scale=2)

#importing a os module which interact with our operating system.
import os
#it will open the file of our qrcode.
os.system("test.png")


