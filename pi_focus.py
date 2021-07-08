import time
import picamera
with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.resolution = (299,299)
    time.sleep(300)
    camera.stop_preview()
quit()
