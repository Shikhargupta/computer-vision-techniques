import numpy as np
import cv2

#Loading the image
img = np.array(cv2.imread('frame00000.jpg',1))

#Converting the colour space from RGB to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Function used to determine the hue value of any colour
red = np.uint8([[[224,206,162 ]]])
print cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

#Defining a range over which target will be searched
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

# Thresholding the HSV image to get only red colors
mask = cv2.inRange(hsv, lower_red, upper_red)

#Finding the mean coordinate
white = []

for i in range(240):
	for j in range(352):
		if mask[i][j] > 0:
			white.append([i,j])

mean1 = np.mean(white, axis=0)

#Drawing the circular marker
cv2.circle(img, (int(mean1[1]),int(mean1[0])), 10, (255,0,0), 0)

cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()