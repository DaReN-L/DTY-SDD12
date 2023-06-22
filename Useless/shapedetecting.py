import cv2 
import imutils 


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):  #method
        shape  = "noen"
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.04 * peri, True)
        if len(approx) ==3:
            shape = "triangle"
        elif len(approx) == 8:
            shape = "octagon"
        elif len(approx) == 7:
             shape = "7sidedshapethingy"
		

        return shape
    

image = cv2.imread(r"C:\Users\Darren\Documents\GitHub\DTY12\Stop-intersection__ResizedImageWzM3NSwyNDBd.jpg")
# image = cv2.imread(r"C:\Users\Darren\Documents\GitHub\DTY12\roadsigns\stopsign.png")
# C:\Users\Darren\Documents\GitHub\DTY12\roadsigns\giveway.png
# C:\Users\Darren\Documents\GitHub\DTY12\roadsigns\Stop_Sign_in_Australia.jpeg
# image = cv2.VideoCapture(0)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3,3),0)
thresh = cv2.threshold(blurred, 110, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

for c in cnts:

	# M = cv2.moments(c)s
	# cX = int((M["m10"] / M["m00"]) * ratio) 
	# cY = int((M["m01"] / M["m00"]) * ratio)
	shape = sd.detect(c)
    
	
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 3)
	cv2.putText(image, shape, (0,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
	# cv2.namedWindow("output", cv2.WINDOW_NORMAL) #To resize the window size of the output 
	
    
	imageRS = cv2.resize(image, (200,120))
	cv2.imshow("Image", imageRS)    
	cv2.imshow("img", thresh)
        
	
	cv2.waitKey(0)