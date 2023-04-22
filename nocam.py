# TESTE (SEM WEBCAM)
import cv2
import pytesseract as pt
import pyttsx3
import math


engine = pyttsx3.init()
voices = engine.getProperty('voices')
#pt.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe")
pt.pytesseract.tesseract_cmd = ("Tesseract-OCR/Tesseract.exe")


config = r'--oem 1 --psm 6 '            # OK:  r'--oem 2 --psm 6'


imagem = cv2.imread("ex3.png")
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, math.pi/180, 200)

angle = lines[0][0][1] * 180 / math.pi

# verificar a orientação da letra na imagem
rect = cv2.minAreaRect(cv2.findNonZero(edges))
if rect[1][0] > rect[1][1]:
    angle -= 90

rows, cols, _ = imagem.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated = cv2.warpAffine(imagem, M, (cols, rows))

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 600, 600)
cv2.namedWindow('Aligned', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Aligned', 600, 600)

cv2.imshow('Original', imagem)
cv2.imshow('Aligned', rotated)
frase = pt.pytesseract.image_to_string(imagem, lang= "por", config = config)
print(frase)

cv2.waitKey(0)
engine.say(frase)
engine.runAndWait()
cv2.destroyAllWindows()













