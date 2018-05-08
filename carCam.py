import cv2
import time
import numpy as np
import os.path

#TODOS:
#   1)Loop 10 second video increments
#   2)Make a log file
#   3)Add text to bottom of video stating date and time
#   4)Be able to shutdown properly
#   5)Log temperature of PI
#   6)Allow pi to sync with home wifi and upload logs


#capture video for a specific amount of seconds and then save it.
def captureVideo(secs):
    #write to file, make sure not to overwrite previous files
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    i =0
    while(os.path.isfile('output%03d.avi'%i)):
        i = i+1
    out = cv2.VideoWriter('output%03d.avi'%i,fourcc, 7.0, (640,480)) #TODO, fix encoder, Playback is janky


    cap = cv2.VideoCapture(0) #capture from main camera
    start_time = time.time()
    end_time = time.time()+secs
    while (int(start_time) < int(end_time)):
        start_time = time.time() #update time each while loop
        ret, img = cap.read()
        if ret == True:
            
            out.write(img)
            
            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break


    cap.release()
    cv2.destroyAllWindows()

captureVideo(2)
