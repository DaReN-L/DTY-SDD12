import cv2
import tkinter as tk  
import time 
import numpy as np
from PIL import ImageGrab

# Stop Sign Cascade Classifier xml
stop_sign = cv2.CascadeClassifier('cascade_stop_sign.xml')
speed_limit = cv2.CascadeClassifier('speedlimitcascade.xml')
stopsignfound = False

# cap = np.array(ImageGrab.grab(bbox=(1000,1000,1800,1600)))
    
    

cap = cv2.VideoCapture(0)   
_,img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
# speed_sign_scaled = speed_limit.detectMultiScale(gray, 1.3, 5)
window = tk.Tk()

window.geometry("800x480") 
window.title ("main screen")
stopimage = tk.PhotoImage(file="roadsigns\stopsign.png")


def settingspage():
    print("settings page pushed")
    setwin = tk.Toplevel(window)
    setwin.geometry("800x480")
    setwin.title("settings page")

    settingstext = tk.StringVar()
    brightnesstext = tk.StringVar()
    settingstext.set("Settings Page")
    brightnesstext.set("Brightness Settings")
    

    def brightness_slider(val):
        print(str(val))
    lightingcontrol = tk.Scale(setwin, from_=0, to=255, orient=tk.HORIZONTAL, width=50, length=500, command=brightness_slider)
    lightingcontrol.pack()


    languagemenu = tk.StringVar(setwin)
    languagemenu.set("English")

    def getlanguage(): 
        print(languagemenu.get())
       
        optionselected = languagemenu.get()
        if optionselected == 'English':
        
            settingstext.set("Settings Page")
            brightnesstext.set("Brightness Settings")
            print("English Checked")
            stopimage = tk.PhotoImage(file="roadsigns\stopsign.png")
            stopsignplace.configure(window, image= stopimage)
              
            
           
        elif optionselected == 'Japanese':
            
            settingstext.set("設定")
            brightnesstext.set("画面の明るさの制御")
            print("Japanese Checked")
            japstopsign= tk.PhotoImage(file="JapStop.gif")
            stopsignplace.configure(window, image= japstopsign)
            
            
            
        
        
        setwin.update()
        
        
    
    tk.Label(setwin, textvariable= settingstext, font= ('Helvetica 24 bold')).pack(pady=30)
    tk.Label(setwin, textvariable= brightnesstext, font=('Helvetica 12 bold')).place(x=2, y=140)
    tk.Label(setwin, image=brightnessimage).place(x=140, y= 120)

    languagedropmenu = tk.OptionMenu(setwin, languagemenu, "English", "Japanese")
    languagedropmenu.pack()

    saveoptionbutton = tk.Button(setwin, text="Save", font= ('Helvetica 18 bold'), command=getlanguage)

    
    def return2main():
        setwin.destroy()
        # tk.Toplevel(window)
        window.update()


    returnbutton = tk.Button(setwin, image=returnimage, height = 60, width= 60, command=return2main)
    returnbutton.place(x=0,y=420)
    lightingcontrol.place(x=200, y=100)
    languagedropmenu.place(x=400, y=200)
    saveoptionbutton.place(x=400, y=250)
    
    setwin.mainloop()

while quit == False:
    window.update()
    time.sleep(2)



for i in stop_sign_scaled:
    print(i)
    print("found one")
    stopsignfound = True
    window.update()

    

    
returnimage=tk.PhotoImage(file="returnimage.gif")
brightnessimage= tk.PhotoImage(file="brightnessimage.gif")
settingsimage = tk.PhotoImage(file="settingsimage.gif")
settings = tk.Button(window, image=settingsimage, height=60, width=60, command=settingspage)
settings.place(x=740, y=420)

stopsignplace=tk.Label(window, image=stopimage)
if stopsignfound == True:   
    stopsignplace.place(x=200, y=180)
else:
    #add timer here later 
    stopsignplace.destroy()




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





