import cv2

# index 0 is the default camera
cam =cv2.VideoCapture(0)

while cam.isOpened():
    state,img = cam.read()
    if not state:
        print("=> Could not read camera")
        break
    cv2.imshow("out",img)
    if cv2.waitKey(1)==27:
        break
cam.release()
cv2.destroyAllWindows()