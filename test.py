import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    "C:/Program Files/Tesseract-OCR/tesseract.exe"
    
image_filename = "image.jpg"
image = cv2.imread(image_filename)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

scale_percent = 200  # เพิ่มขนาด 2 เท่า (200%)
width = int(gray_image.shape[1] * scale_percent / 100)
height = int(gray_image.shape[0] * scale_percent / 100)
dim = (width, height)
upscaled_image = cv2.resize(gray_image, dim, interpolation=cv2.INTER_CUBIC)

text = pytesseract.image_to_string(upscaled_image, lang='tha')

print(text)

cv2.imshow("Image", upscaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()