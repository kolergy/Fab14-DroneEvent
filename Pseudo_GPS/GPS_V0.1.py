# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import datetime
import cv2

def show(name, img, x, y):
    cv2.namedWindow( name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, x, y)
    cv2.imshow(name, img)


cam = np.load('camera_matrix.npy')
coef = np.load('dist_coefs.npy')


def undistort(img, camera_matrix, dist_coefs):
    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))
    #undistort
    img = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)
    #crop 
    x, y, w, h = roi
    img = img[y:y+h, x:x+w]
    return img
    
h = 640 * 2
v = 480 * 2

# initialize the camera and grab a reference to the raw camera capture
camera            = PiCamera()
camera.resolution = (h,v)
camera.framerate  = 32
rawCapture        = PiRGBArray(camera, size= (h,v))
fgbg              = cv2.createBackgroundSubtractorMOG2()

# allow the camera to warmup
time.sleep(1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    #Capture	    
    start  = time.time()
    img    = frame.array # grab an image from the pi camera
    capture_time = time.time() - start

    tscpt  = datetime.datetime.fromtimestamp(capture_time) # the timestamp of the capture
    
    #undistort
    img = undistort(img, cam, coef)
    undistort_time = time.time() - capture_time
    
    #blu    = cv2.medianBlur(img, 3)
    #blt    = time.time()
    #bltime = blt - cpt
    #sblu   = cv2.resize(blu, (640,480), interpolation=cv2.INTER_AREA)
    #ret    = time.time()
    #retime = ret - blt 
    #fgmask = fgbg.apply(sblu)
    
    
    # Apply MOG2
    fgmask = fgbg.apply(img)
    
    mot    = cv2.bitwise_and(img,img,mask=fgmask)
    hsv    = cv2.cvtColor(mot, cv2.COLOR_BGR2HSV) # convert to hsv 
    MOG2_time = time.time() - undistort_time     
    
    
    # apply color mask
    lgreen = np.array([ 50, 0,160]) 
    hgreen = np.array([90,180,255])
    mask   = cv2.inRange(hsv, lgreen, hgreen)
    cimg, cont, hie = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    color_mask_time = time.time() - MOG2_time
    
    
    # Fiding point of interest
    le = len(cont)
    print("len: "+ str(le))
    
    if le > 0:
        for c in cont:
            ((cx,cy), r) = cv2.minEnclosingCircle(c)
            if r > 3:
                print("cx: " + str(cx) + "\t cy: " + str(cy) + "\t Rad: " + str(r))
                #cv2.drawContours(mask, mc, -1, (255,255,0), 3)
                cv2.circle(mot, (int(cx), int(cy)), int(r+5), (0, 255, 255), 2)
    
    
    find_time = time.time() - color_mask_time
    
    
    end = time.time()
    # cleaned image
    #cle = cv2.bitwise_and(mot,mot,mask=mask)

    
    
    print("total time : " + str(end - start))
    print("capture time : " + str(capture_time))
    print("MOG2 time : " + str(MOG2_time))
    print("color_mask time : " + str(color_mask_time))
    print("find time : " + str(find_time))
    
    # display the image on screen and wait for a keypress
    show(   "mot",   img, 640, 480)
    #show("fgmask",fgmask, 640, 480)
    show(  "mask",  mask, 640, 480)
    #show( "cont",   cont, 640, 480)
    k = cv2.waitKey(1)
    rawCapture.truncate(0)
    if k == ord('q'):
        break

cv2.destroyAllWindows

