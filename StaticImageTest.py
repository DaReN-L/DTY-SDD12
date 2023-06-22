import cv2 
from matplotlib import pyplot as plt 
from PIL import ImageGrab
import numpy as np
import tkinter as tk 
from tkinter import *

#beware this is a prototype and is not a part of the final product, this is to just prove the evidence in developments and working

img = cv2.imread(r"") #image input, only works with absolute paths, there are sample images in the folder.

# img = np.array(ImageGrab.grab(bbox=(0,40,800,640)))  #video didn't work 
# img = cv2.VideoCapture(0) #live camera didn't work
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert image to grat 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #convert image to RGB
  

stop_data = cv2.CascadeClassifier('cascade_stop_sign.xml') #cascade data 
  
found = stop_data.detectMultiScale(img_gray,                #detect function
                                   minSize =(20, 20)) 
  
amount_found = len(found) 

if amount_found != 0: 
      
    # There may be more than one 
    # sign in the image 
    for (x, y, width, height) in found: #drawing box around the found o bject. 
          
    
        cv2.rectangle(img_rgb, (x, y),  #properties of the rectangle 
                      (x + height, y + width),  
                      (0, 255, 0), 5) 
        print("Found one")

# window = tk.Tk()

# window.geometry("800x480") 
# window.title ("main screen")

# def settingspage():
#     print("settings page pushed")
#     setwin = Toplevel(window)
#     setwin.geometry("800x480")
#     setwin.title("settings page")

#     Label(setwin, text= "Settings Page", font= ('Helvetica 24 bold')).pack(pady=30)
#     # Label(setwin, text= "Brightness Control", font=('Helvetica 12 bold')).place(x=50, y=140)
#     Label(setwin, image=brightnessimage).place(x=140, y= 120)


#     lightingcontrol = Scale(setwin, from_=0, to=255, orient=HORIZONTAL, width=50, length=500)

#     langugemenu = StringVar()
#     langugemenu.set("Select Language")

#     languagedropmenu = OptionMenu(setwin, langugemenu, "English", "Japanese")
#     languagedropmenu.pack()
    
#     def saveoption(languagemenu):
#         selection=languagemenu.get()
#         print(selection)

#     saveoptionbutton = Button(setwin, text= "Save", height=10, width=25, commend=saveoption)

#     def return2main():
#         setwin.destroy()
#         window = Toplevel(window)

    
#     returnbutton = Button(setwin, image=returnimage, height = 60, width= 60, command=return2main)
#     returnbutton.place(x=0,y=420)
#     lightingcontrol.place(x=200, y=100)
#     languagedropmenu.place(x=400, y=200)
#     saveoptionbutton.place(x=400, y=250)

    
    


    
# returnimage=PhotoImage(file="returnimage.gif")
# brightnessimage= PhotoImage(file="brightnessimage.gif")
# settingsimage = PhotoImage(file="settingsimage.gif")
# settings = Button(window, image=settingsimage, height=60, width=60, command=settingspage)
# stopimage = PhotoImage(file="roadsigns\stopsign.png")

# settings.place(x=740, y=420)
# if amount_found >= 1:
#     Label(image=stopimage).place(x=200, y=180)




# window.mainloop()  
        


# cv2.imshow('window', img_rgb)
# cv2.waitKey(0)

plt.subplot(1, 1, 1) 
plt.imshow(img_rgb) #showing the image and the detection rectangle on a window 
plt.show() 




