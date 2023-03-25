import cv2

# index 0 is the default camera
cam =cv2.VideoCapture(0)
fcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("camera_record.avi",fcc,30.0,(640,480))

while cam.isOpened():
    state,img = cam.read()
    if not state:
        print("=> Could not read camera")
        break
    cv2.imshow("out",img)
    out.write(img) #^ put the image in the video
    if cv2.waitKey(1)==27:
        break
cam.release()
out.release() #! save the video
cv2.destroyAllWindows()