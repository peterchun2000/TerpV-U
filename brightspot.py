import cv2 
import numpy as np

image = cv2.imread("brightspot.png")

#  constants
BINARY_THRESHOLD = 20
CONNECTIVITY = 4
DRAW_CIRCLE_RADIUS = 4

#  convert to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#  extract edges
binary_image = cv2.Laplacian(gray_image, cv2.CV_8UC1)

#  fill in the holes between edges with dilation
dilated_image = cv2.dilate(binary_image, np.ones((5, 5)))

#  threshold the black/ non-black areas
_, thresh = cv2.threshold(dilated_image, BINARY_THRESHOLD, 255, cv2.THRESH_BINARY)

#  find connected components
components = cv2.connectedComponentsWithStats(thresh, CONNECTIVITY, cv2.CV_32S)

#  draw circles around center of components
#see connectedComponentsWithStats function for attributes of components variable
centers = components[3]
for center in centers:
    cv2.circle(thresh, (int(center[0]), int(center[1])), DRAW_CIRCLE_RADIUS, (255), thickness=-1)

cv2.imwrite("res.png", thresh)
cv2.imshow("result", thresh)
cv2.waitKey(0)