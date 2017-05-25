import cv2
import numpy as np

#Reading the image in RGB format so that coloured contours can be drawn.
img1 = cv2.imread('hex.pgm', 1)

#Reading the image in grayscale.
img = cv2.imread('hex.pgm',0)

#Thresholding the image to remove unwanted features as much as possible keeping the hexagons.
_,thresh = cv2.threshold(img,80,255,0) #lower bound on thresholding found by hit and trial.
cv2.imwrite('thresh.jpg', thresh)

#Finding the contours in the thresholded image and storing them in an array.
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)

#Finding the area of all the contours and storing them in an array.
area = []
for c in contours:
	ar = cv2.contourArea(c)
	area.append(ar)

#Sorting the contours according to the area (descending order).
sorteddata = sorted(zip(area, contours), key=lambda x: x[0], reverse=True)

#Picking only the largest 6 contours of the 6 hexagons. Rest are of no use.
largestcontour = []
for i in range(6):
	largestcontour.append(sorteddata[i][1])

#Drawing the contours
cv2.drawContours(img1,largestcontour,-1,(255,0,0),10)

#Saving the image
cv2.imwrite("th.jpg", img1)
