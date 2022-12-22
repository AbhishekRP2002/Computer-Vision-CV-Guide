import cv2
import cv2
import pytesseract


def ocr_core(img):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img ,config='--psm 11')
    return text

img = cv2.imread('test1.png')

#get gray scale image
def get_gray_scale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Remove noise from image
def remove_noise(image):
    return cv2.medianBlur(image,5)

#Thresholding - if the pixel value is less than threshold , then it is white else black

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = get_gray_scale(img)
img = thresholding(img)
img=  remove_noise(img)

print(ocr_core(img))
