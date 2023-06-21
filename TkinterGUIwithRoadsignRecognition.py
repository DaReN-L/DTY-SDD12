import tkinter as tk  
import cv2
import time 
import numpy as np
from PIL import ImageGrab
from rpi_backlight import Backlight
# Stop Sign and speed limit Cascade Classifier xml, these are datasets for HAAR 
stop_sign = cv2.CascadeClassifier('cascade_stop_sign.xml')          
speed_limit = cv2.CascadeClassifier('speedlimitcascade.xml')
stopsignfound = False

# cap = np.array(ImageGrab.grab(bbox=(1000,1000,1800,1600)))

    
window = tk.Tk() #Tkinter Window

window.geometry("800x480") 
window.title ("main screen")    
stopimage = tk.PhotoImage(file="roadsigns\stopsign.png")


cap = cv2.VideoCapture(0)       #OpenCV Video Input
_,img = cap.read()  #OpenCV reading video
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #converting image to gray and white
stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5) #detecting object within image




def settingspage(): #Tkinter Settings page
    # print("settings page pushed")
    setwin = tk.Toplevel(window)    #settings window properties
    setwin.geometry("800x480")
    setwin.title("settings page")

    settingstext = tk.StringVar()   #labels and texts
    brightnesstext = tk.StringVar()
    settingstext.set("Settings Page")
    brightnesstext.set("Brightness Settings")
    
    
    def brightness_slider(val): #brightness settings
        print(str(val))
    lightingcontrol = tk.Scale(setwin, from_=0, to=255, orient=tk.HORIZONTAL, width=50, length=500, command=brightness_slider)
    lightingcontrol.pack()


    languagemenu = tk.StringVar(setwin) #dropdown menu
    languagemenu.set("English")

    def getlanguage(): #pull data from drop down menu
        print(languagemenu.get())
       
        optionselected = languagemenu.get()
        if optionselected == 'English': #Things that will happen when I select English
        
            settingstext.set("Settings Page") 
            brightnesstext.set("Brightness Settings")
            print("English Checked")
            stopimage = tk.PhotoImage(file="roadsigns\stopsign.png")
            stopsignplace.config(image= stopimage)  
           
        elif optionselected == 'Japanese':  #Things that will happend when I select Japanese
            
            settingstext.set("設定")
            brightnesstext.set("画面の明るさの制御")    #changing texts to japanese 
            print("Japanese Checked")
            japstopsign= tk.PhotoImage(file="JapStop.gif")  #changing the road signs into japanese roadsigns 
            stopsignplace.config(image= japstopsign)         
        
        
        setwin.update() #update the window to display the newest lanaguge 
        
        
    
    tk.Label(setwin, textvariable= settingstext, font= ('Helvetica 24 bold')).pack(pady=30) #placements for texts
    tk.Label(setwin, textvariable= brightnesstext, font=('Helvetica 12 bold')).place(x=2, y=140)
    tk.Label(setwin, image=brightnessimage).place(x=140, y= 120)

    languagedropmenu = tk.OptionMenu(setwin, languagemenu, "English", "Japanese")   #drop down menu selections 
    languagedropmenu.pack()

    saveoptionbutton = tk.Button(setwin, text="Save", font= ('Helvetica 18 bold'), command=getlanguage)

    
    def return2main(): #return to main page button
        setwin.destroy()
        # tk.Toplevel(window)
        window.update()


    returnbutton = tk.Button(setwin, image=returnimage, height = 60, width= 60, command=return2main) #placements 
    returnbutton.place(x=0,y=420)
    lightingcontrol.place(x=200, y=100)
    languagedropmenu.place(x=400, y=200)
    saveoptionbutton.place(x=400, y=250)
    
    setwin.mainloop()


for i in stop_sign_scaled: #if openCV found a stop sign, it changes the boolean to TRUE and stop sign should display on main page
    # print(i)
    # print("found one")
    stopsignfound = True
    window.update()

def quickbrightnessset(): #quick tunnel brightness settings
    tunnelbrightness = 20
    surfacebrightness = 100
    if Backlight.brightness > tunnelbrightness:
        Backlight.brightness = surfacebrightness
    elif Backlight.brightness < surfacebrightness:
        Backlight.brightness = tunnelbrightness


returnimage=tk.PhotoImage(file="returnimage.gif")   #images properties in TKinter 
brightnessimage= tk.PhotoImage(file="brightnessimage.gif")
settingsimage = tk.PhotoImage(file="settingsimage.gif")
settings = tk.Button(window, image=settingsimage, height=60, width=60, command=settingspage) #button properties 
quickbrightness=tk.Button(window, image=brightnessimage,height=60, width=60)
quickbrightness.place(x=740, y=420) #placements 
settings.place(x=0,y=420)

stopsignplace=tk.Label(window, image=stopimage)
if stopsignfound == True:   #place the stop sign image if the boolean is True 
    stopsignplace.place(x=200, y=180)
    window.update()
else:
    time.sleep(5) 
    stopsignplace.destroy() #stop sign image disappears after not detected for 5 seconds 


quit = False

while quit == False: #while the program is not quit, the window updates every 2 seconds. 
    window.update()
    print("update")
    time.sleep(2)
    

window.mainloop() 



    # Detect the stop sign, x,y = origin points, w = width, h = height
    # for (x, y, w, h) in stop_sign_scaled:
    #     # Draw rectangle around the stop sign
    #     stop_sign_rectangle = cv2.rectangle(img, (x,y),
    #                                         (x+w, y+h),
    #                                         (0, 255, 0), 3)
    #     # Write "Stop sign" on the bottom of the rectangle
    #     stop_sign_text = cv2.putText(img=stop_sign_rectangle,
    #                                  text="Stop Sign",
    #                                  org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    #                                  fontScale=1, color=(0, 0, 255),
    #                                  thickness=2, lineType=cv2.LINE_4)
    #     print("found one")
    #     stopsignfound = True
    # for (x, y, w, h) in speed_sign_scaled:
    #     speed_sign_rectangle = cv2.rectangle(img, (x,y),
    #                                         (x+w, y+h),
    #                                         (0, 255, 0), 3)
        
    #     stop_sign_text = cv2.putText(img=speed_sign_rectangle,
    #                                  text="Speed limit Sign",
    #                                  org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    #                                  fontScale=1, color=(0, 0, 255),
    #                                  thickness=2, lineType=cv2.LINE_4)
        
    #     print("found one")
        

        
        
        

    # for i in speed_sign_scaled:
    #     print(i)
    #     print("found one")

    # cv2.imshow("img", img)
    # key = cv2.waitKey(30)
    # if key == ord('q'):
    #     cap.release()
    #     cv2.destroyAllWindows()





