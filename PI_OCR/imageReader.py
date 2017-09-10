from .TrainAndTest import findString
import time
import picamera
import picamera.array
import cv2

def capture():
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            camera.capture(stream, format='bgr')
            # At this point the image is available as stream.array
            image = stream.array
            return(image)

def determineString(image):
    result = findString(image)
    return(result)
if __name__ == "__main__":
    print(determineString(capture()))