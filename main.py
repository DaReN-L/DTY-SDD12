
import numpy as np
from PIL import ImageGrab
import cv2

def draw_lines(image,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(image, (coords[0], coords[1]),(coords[2], coords[3]), [0,255,0], 3)
    except:
        pass
    
        


def roi(image, vertices): #region of interests 
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked


def process_img(image):
    processed_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    # processed_image = cv2.GaussianBlur(processed_image, (5,5),0)
    vertices = np.array([[10,500],[10,300], [300,200], [500,200], [800,300],[800,500]])
    processed_image = roi(processed_image, [vertices])

    lines = cv2.HoughLinesP(processed_image, 1, np.pi/180, 180, 100, 5)
    draw_lines(processed_image,lines) 


    return processed_image

#streaming the screen
while True: 
    screen = np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    
    
    new_screen = process_img(screen)
    # cv2.imshow('window2',cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2RGB))
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break                   #Its lagging really bad, probably loop time too long