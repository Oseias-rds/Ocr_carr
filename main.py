import cv2
import pytesseract as tss


def img_to_text():
    
    img = cv2.imread("d.jpg")
    resultado = tss.image_to_string(img)
    print(resultado)

img_to_text()