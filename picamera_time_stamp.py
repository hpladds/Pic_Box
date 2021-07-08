import time
import picamera
with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.resolution = (299,299)
    try:
       for i, filename in enumerate(camera.capture_continuous('../Camera_Pix/image{timestamp:%H-%M-%S-%f}.jpg')):
            print(filename)
            time.sleep(.5)
            if i == 40:
                break
    finally:
        camera.stop_preview()
quit()
