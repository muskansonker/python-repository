import cv2
import numpy as np
#tessersct library
cam=cv2.VideoCapture(0)

while cam.isOpened():
    state,img=cam.read()
    # resize image
    img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
    #filter
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    gray3=np.stack((gray,)*3,axis=-1)
    #grid 
    row1=np.hstack((img,rgb))
    row2=np.hstack((gray3,hsv))
    output=np.vstack((row1,row2))
    #output=np.hstack((img,rgb,hsv))
    cv2.imshow("out",output)
    if cv2.waitKey(1)==27:
        break
cam.release()
cv2.destroyAllWindows()