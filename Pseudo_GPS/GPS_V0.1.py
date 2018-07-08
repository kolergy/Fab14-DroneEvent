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

h = 640 * 2
v = 480 * 2

# initialize the camera and grab a reference to the raw camera capture
camera            = PiCamera()
camera.resolution = (h,v)
camera.framerate  = 32
rawCapture        = PiRGBArray(camera, size= (h,v))
fgbg              = cv2.createBackgroundSubtractorMOG2()

# allow the camera to warmup
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):    # grab an image from the pi camera & convert to hsv 
    #camera.capture(rawCapture, format="bgr")
    #image  = rawCapture.array
    start  = time.time()
    img    = frame.array
    blu    = cv2.medianBlur(img, 3)
    sblu   = cv2.resize(blu, (640,480), interpolation=cv2.INTER_AREA)
    fgmask = fgbg.apply(sblu)
    mot    = cv2.bitwise_and(sblu,sblu,mask=fgmask)
    hsv    = cv2.cvtColor(mot, cv2.COLOR_BGR2HSV)

    # create a mask
    lgreen = np.array([ 50, 0,160]) 
    hgreen = np.array([90,180,255])
    mask   = cv2.inRange(hsv, lgreen, hgreen)
    cont   = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    le = len(cont)
    print(le)
    cv2.drawContours(mask, cont, -1, (255,255,0), 3)
    # cleaned image
    #cle = cv2.bitwise_and(mot,mot,mask=mask)
    end = time.time()
    print(end - start)
    # display the image on screen and wait for a keypress
    show(   "mot",   mot, 640, 480)
    #show("fgmask",fgmask, 640, 480)
    show(  "mask",  mask, 640, 480)
    show( "cont",   cont, 640, 480)
    k = cv2.waitKey(1)
    rawCapture.truncate(0)
    if k == ord('q'):
        break
cv2.destroyAllWindows

