# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2

def show(name, img, x, y):
    cv2.namedWindow( name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, x, y)
    cv2.imshow(      name,  img)
 
# initialize the camera and grab a reference to the raw camera capture
camera            = PiCamera()
camera.resolution = (640,480)
camera.framerate  = 32
rawCapture        = PiRGBArray(camera, size= (640,480))
fgbg              = cv2.createBackgroundSubtractorMOG2()

# allow the camera to warmup
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):    # grab an image from the pi camera & convert to hsv 
    #camera.capture(rawCapture, format="bgr")
    #image  = rawCapture.array
    image  = frame.array
    fgmask = fgbg.apply(image)
    mot    = cv2.bitwise_and(image,image,mask=fgmask)
    med    = cv2.medianBlur(mot, 3)
    hsv    = cv2.cvtColor(med, cv2.COLOR_BGR2HSV)

    # create a mask
    lgreen = np.array([ 50, 0,160]) 
    hgreen = np.array([90,180,255])
    mask   = cv2.inRange(hsv, lgreen, hgreen)

    # cleaned image
    cle = cv2.bitwise_and(med,med,mask=mask)

    # display the image on screen and wait for a keypress
    show(   "mot",   mot, 640, 480)
    show("fgmask",fgmask, 640, 480)
    show(  "mask",  mask, 640, 480)
    show( "clean",   cle, 640, 480)
    k = cv2.waitKey(1)
    rawCapture.truncate(0)
    if k == ord('q'):
        break
cv2.destroyAllWindows

