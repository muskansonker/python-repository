import streamlit as st
from orm import Image,create_engine
from sqlalchemy.orm import sessionmaker
import cv2
from PIL import Image

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
# load an image from device
img4=Image.open(r'C:\Users\hp\Documents\Python\papp\pokemon.jpg')
img4

def opendb():
    engine=create_engine('sqlite:///db.sqlite',echo=True)
    Session=sessionmaker(bind=engine)
    sess=Session()
    return sess

def closedb(sess):
    sess.commit()
    sess.close()

def add_image(image_name):
    db=opendb()
    obj=Image(name=image_name)
    db.add(obj)
    closedb(db)

def view_Images():
    db=opendb()
    images=db.query(Image).all()
    return images

st.title("Face Recognization")

#! add Image
form=st.form(key='add_image')
name=form.text_input(label='Image Person Name')
size=form.text_input(label='Size')
submit=form.form_submit_button(label='Add Image ')
if submit:
    add_image(name)