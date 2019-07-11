# coding=utf-8
import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r""

images = Image.open('/home/jason/图片/image.png')

text = pytesseract.image_to_string(images, lang='chi_sim')
print(text)