import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    "C:/Program Files/Tesseract-OCR/tesseract.exe"
    
image_filename = "image.jpg"
image = cv2.imread(image_filename)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

denoised = cv2.medianBlur(gray_image, 3)


text = pytesseract.image_to_string(denoised, lang='tha')

print(text)

cv2.imshow("Image", denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()