from PIL import Image
import pytesseract

text = pytesseract.image_to_string("/home/manoj/Python_App/ETL/image/img.jpg")
print(text)