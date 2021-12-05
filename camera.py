import picamera
from time import sleep
def film():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_recording('film.h264')
    camera.wait_recording(10)
    camera.stop_recording()

def photo(image):
    camera=picamera.PiCamera()
    camera.start_preview()
    sleep(1)
    camera.capture(image)
    camera.stop_preview()
