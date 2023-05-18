import cv2 
from matplotlib import pyplot as plt 
from PIL import ImageGrab
import numpy as np
import tkinter as tk 
from tkinter import *



img = cv2.imread(r"C:\Users\Darren\Documents\GitHub\DTY12\Stop-intersection__ResizedImageWzM3NSwyNDBd.jpg")
#C:\Users\Darren\Documents\GitHub\DTY12\Stop-intersection__ResizedImageWzM3NSwyNDBd.jpg
# img = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
# img = cv2.VideoCapture(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  
  
# Use minSize because for not  
# bothering with extra-small  
# dots that would look like STOP signs 
stop_data = cv2.CascadeClassifier('stop_data.xml') 
  
found = stop_data.detectMultiScale(img_gray,  
                                   minSize =(20, 20)) 
  
# Don't do anything if there's  
# no sign 
amount_found = len(found) 

if amount_found != 0: 
      
    # There may be more than one 
    # sign in the image 
    for (x, y, width, height) in found: #drawing box around the found o bject. 
          
    
        cv2.rectangle(img_rgb, (x, y),  
                      (x + height, y + width),  
                      (0, 255, 0), 5) 
        print("Found one")

window = tk.Tk()

window.geometry("800x480") 
window.title ("main screen")

def settingspage():
    print("settings page pushed")
    setwin = Toplevel(window)
    setwin.geometry("800x480")
    setwin.title("settings page")

    Label(setwin, text= "Settings Page", font= ('Helvetica 24 bold')).pack(pady=30)
    # Label(setwin, text= "Brightness Control", font=('Helvetica 12 bold')).place(x=50, y=140)
    Label(setwin, image=brightnessimage).place(x=140, y= 120)


    lightingcontrol = Scale(setwin, from_=0, to=255, orient=HORIZONTAL, width=50, length=500)


    def return2main():
        setwin.destroy()
        window = Toplevel(window)

    returnbutton = Button(setwin, text="Return", height = 60, width= 8, command=return2main)
    returnbutton.place(x=0,y=420)
    lightingcontrol.place(x=200, y=100)


    

brightnessimage= PhotoImage(file="brightnessimage.gif")
settingsimage = PhotoImage(file="settingsimage.gif")
settings = Button(window, image=settingsimage, height=60, width=60, command=settingspage)
stopimage = PhotoImage(file="roadsigns\stopsign.png")

settings.place(x=740, y=420)
if amount_found >= 1:
    Label(image=stopimage).place(x=200, y=180)




window.mainloop()  
        


cv2.imshow('window', img_rgb)
cv2.waitKey(0)

# plt.subplot(1, 1, 1) 
# plt.imshow(img_rgb) 
# plt.show() 




