from PIL import Image
from pytesseract import pytesseract


img = Image.open('Capture.PNG')

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Passing the image object to image_to_string() function to extract the text from image
text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text)