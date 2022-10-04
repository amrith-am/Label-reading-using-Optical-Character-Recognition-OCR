try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


info = recText('TEST2.png')
print(info)
file = open("result.txt", "w")
file.write(info)
file.close()
print("Written Successful")
