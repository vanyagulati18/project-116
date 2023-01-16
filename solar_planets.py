import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Mercury",(110,170),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))
cv2.putText(img,"Venus",(200,170),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))
cv2.putText(img,"Earth",(300,170),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))
cv2.putText(img,"Mars",(400,170),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))
cv2.putText(img,"Jupiter",(600,100),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))
cv2.putText(img,"Saturn",(780,120),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))
cv2.putText(img,"Uranus",(980,120),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))
cv2.putText(img,"Neptune",(1100,120),fontFace=cv2.FONT_ITALIC, fontScale=0.4, color=(0,0,255))

cv2.imshow("output",img)


cv2.waitKey(0)