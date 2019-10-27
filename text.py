from PIL import Image
#import tesseract-ocr
import pytesseract
print(pytesseract.image_to_string(Image.open('pancard.jpg')))



