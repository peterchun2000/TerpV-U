import cv2
import numpy as np

img = cv2.imread('brightspot.png')
img = cv2.resize(img,(400,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,gray = cv2.threshold(gray,127,255,0)
gray2 = gray.copy()
mask = np.zeros(gray.shape,np.uint8)

contours, hier = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if 200<cv2.contourArea(cnt)<5000:
        cv2.drawContours(img,[cnt],0,(0,255,0),2)
        cv2.drawContours(mask,[cnt],0,255,-1)
cv2.bitwise_not(gray2,gray2,mask)

cv2.imshow('IMG',gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()