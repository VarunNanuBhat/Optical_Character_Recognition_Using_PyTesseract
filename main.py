import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

'''
Function to return test in image
'''
def ocr(img):
    text = pytesseract.image_to_string(img)
    print("entered")
    return text

img = cv2.imread('Capture.PNG')
'''
Function to pre-process the image to increase accuracy 
'''

def convert_image_to_greyscale(imgage):
    return cv2.cvtColor(imgage, cv2.COLOR_RGB2GRAY)


'''
thresholding - we need to have threshold which states that 
if pixel value is above a certain threshold, 
then the image is black. 
In this case, we will have a concrete black and white image,
which will yield better results.
'''

def thresholding(imgage):
    return cv2.threshold(imgage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


'''
Function to remove noise and increase sharpness of image 
'''

def remove_noise(imgage):
    return cv2.medianBlur(imgage, 5)


# calling the functions
img = convert_image_to_greyscale(img)
img = thresholding(img)
img = remove_noise(img)


print(ocr(img))
print("done")


