import cv2


stop_sign = cv2.CascadeClassifier('cascade_stop_sign.xml')
ped_crossing_sign = cv2.CascadeClassifier('ped_crossing_cascade2.xml')
school_zone_sign = cv2.CascadeClassifier('school_zone_cascade2.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 2, 5)
    ped_cross_scaled = ped_crossing_sign.detectMultiScale(gray, 2.3, 5)
    school_zone_scaled = school_zone_sign.detectMultiScale(gray, 2.3, 5)

    
    for (x, y, w, h) in stop_sign_scaled:
        
        stop_sign_rectangle = cv2.rectangle(img, (x,y),
                                            (x+w, y+h),
                                            (0, 255, 0), 3)
        
        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                     text="Stop Sign",
                                     org=(x, y+h+30),
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1, color=(0, 0, 255),
                                     thickness=2, lineType=cv2.LINE_4)  
        
    for (x, y, w, h) in ped_cross_scaled:
        
        stop_sign_rectangle = cv2.rectangle(img, (x,y),
                                            (x+w, y+h),
                                            (0, 255, 0), 3)
        
        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                     text="Pedestrian Crossing",
                                     org=(x, y+h+30),
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1, color=(0, 0, 255),
                                     thickness=2, lineType=cv2.LINE_4)  
        
    for (x, y, w, h) in school_zone_scaled:
        
        stop_sign_rectangle = cv2.rectangle(img, (x,y),
                                            (x+w, y+h),
                                            (0, 255, 0), 3)
        
        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                     text="School Zone",
                                     org=(x, y+h+30),
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1, color=(0, 0, 255),
                                     thickness=2, lineType=cv2.LINE_4)  
        
    for i in stop_sign_scaled:
        print(i)
        print("found stop sign")
    for i in ped_cross_scaled:
        print(i)
        print("found pedestrian crossing sign")
        print("Bump ahead")
        print("reduce speed to 25km/h")
    
    for i in school_zone_scaled:
        print(i)
        print("School Zone Detected")
        print("Check Time")
        print("Reduce Speed to 40km/h")
    cv2.imshow("img", img)
    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break