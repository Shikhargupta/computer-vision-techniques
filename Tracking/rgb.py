import cv2
import numpy as np

#Iterarting through all the images
for k in range(0,1):
	print k
	img = np.array(cv2.imread('frame' + str("%05d"%k) + '.jpg',1))

	#Separating the blue, green and red channels from the image
	b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]

	#Determining the size of the image
	row = np.shape(b)[0]
	column = np.shape(b)[1]

	#Initializing the channel for storage of pixel values after removing the green and blue components from the red channel
	only_red = np.zeros((row,column))

	#Iterating through the pixels
	for i in range(row):
		for j in range(column):
			#Subtracting the green and blue components from the red channel
			temp = r[i][j]
			temp2 = 0.7*b[i][j] + g[i][j]*0.7 #Factor of 0.7 estimated by hit and trial
			#Some conditions to prevent overflow
			if temp2>255:
				temp2 = 255
			if temp2>temp:
				only_red[i][j] = 0
			else:
				only_red[i][j] = temp - temp2
			
	#Cropping the image to remove noise	at the edges		
	only_red = only_red[0:475,0:640]

	#Initializing the list of set of coordinates with pixel value greater than 0
	white = []

	for i in range(470):
		for j in range(640):
			if only_red[i][j] > 0:
				white.append([i,j])

	#calculating the mean of the set of coordinates			
	mean1 = np.mean(white, axis=0)	

	#Circular marker with mean point as the center
	cv2.circle(img, (int(mean1[1]),int(mean1[0])), 10, (255,0,0), 0)

	#Saving the result image with the marker on the red vehicle
	cv2.imwrite('result/' + str(k) + '.png', img)
	cv2.imwrite('result1.png', only_red)