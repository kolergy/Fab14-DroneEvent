import picamera
import datetime

now = datetime.datetime.now()

print(now.isoformat())

exit
with picamera.PiCamera() as camera:
    camera.resolution = (640*2, 480*2)
    camera.start_recording(now.isoformat() + '.h264')
    camera.wait_recording(600)
    camera.stop_recording()
