import cv2

# index 0 is the default camera
cam =cv2.VideoCapture(0)
img_counter=0
while cam.isOpened():
    state,img = cam.read()
    if not state:
        print("=> Could not read camera")
        break
    cv2.imshow("out",img)
    if cv2.waitKey(1)==27:
        break
    elif cv2.waitKey(1)==32:
        img_name="opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,img)
        print("snapshot taken")
        img_counter+=1
cam.release()
cv2.destroyAllWindows()