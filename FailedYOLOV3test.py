import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
whT = 320

classNames = ['cars', 'traffic light', 'person']

modelConfiguration = 'yolov3.cfg'
modelWeights = 'yolov3.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


while True: 
    success, img = cap.read()
 
    blob = cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crp=False)
    net.setInput(blob)

    layerName = net.getLayerNames()
    print(layerName)
    print(outputNames)
    print (net.getUnconnectedOutLayers())

    outputNames = [layerName[i[0]-1] for i in net.getUnconnectedOutLayers()]

    outputs = net.forward(outputNames)
    print(outputs[0].shape)

    cv2.imshow('Image', img)
    cv2.waitKey(1) 


