import cv2
import time
import numpy as np
import random
import imageio
import numpy as np

camModel = subprocess.run("cat /sys/class/video4linux/*/name | awk '/Video Capture 4/ || /mxc-mipi-csi2.1/ {print $1}'", shell=True, stdout=subprocess.PIPE, universal_newlines=True).stdout.rstrip('\n')
if (camModel == "Video"):
    print("USB-CAMERA DETECTED")
#    	
    cap = cv2.VideoCapture("v4l2src device=/dev/video2 ! video/x-raw, width=640, height=480, framerate=60/1, format=(string)UYVY ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)  
elif (camModel == "mxc-mipi-csi2.1"):
    print("MIPI-CSI-CAMERA DETECTED")
    cap = cv2.VideoCapture("v4l2src ! video/x-raw, width=640, height=480, framerate=60/1, format=(string)BGRx ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    # mipi
else:
    print("No Camera found")


if not cap.isOpened():
    print("Unable to find camera index")
    exit()
result=True
while (result):
    ret,frame=cap.read()
    
    if not ret:
        print("Can't receive frame")
        break
        
    cv2.imwrite("click69.jpg", frame)
    result=False
cap.release()
cv2.destroyAllWindows()
time.sleep(2)
f=imageio.imread("click69.jpg", as_gray=True)
if np.mean(f) > 60 and np.mean(f) < 225:
    print("Camera is Ready")

else:
    print("Camera is not Ready")
    
