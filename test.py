# some python file
# import textract
# import os
#
# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Tesseract-OCR/'
# text = textract.process("IMG_20170709_155700.jpg")
# print (text.decode("utf-8") )


# import pytesseract
# from PIL import Image
#
# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
# text = pytesseract.image_to_string(Image.open("invoice.jpg"),lang="eng",boxes=False,config="--psm 3 --eom 3")
# print (text)
# new_text = text.replace("\n", "\t")
# #
import cv2

import numpy as np
# Read image
im = cv2.imread("ocr/Tax-invoice-template-final1.jpg")

# Select ROI
r = cv2.selectROI(im)

# Crop image
imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

# Display cropped image
cv2.imshow("Image", imCrop)
cv2.imwrite("working/newimage.jpg", imCrop)
cv2.waitKey(0)

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
text = pytesseract.image_to_string(Image.open("working/newimage.jpg"),lang="eng",boxes=False,config="--psm 3 --eom 3")
print (text)
new_text = text.replace("\n", "\t")
#

# from tabula import read_pdf
# # Read remote pdf into DataFrame
# df2 = read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")
# print (df2)
