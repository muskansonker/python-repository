import cv2
import pytesseract as pt

def ocr_core(img):
    text=pt.image_to_string(img) #* converting image to text
    return text

img=cv2.imread('img.png') #* Load the image

#! get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #* converting image(RGB) to gray image

#& noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5) #* removing noise of image by doing medianBlur

#^ thresholding
def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] #* converting image to binary image

img=get_grayscale(img)
img=thresholding(img)
img=remove_noise(img)

print(ocr_core(img))