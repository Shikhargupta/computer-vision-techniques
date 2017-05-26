import cv2
import numpy as np
import pylab as pl
import glob
import pandas as pd

# define gabor filter bank with different orientations and at different scales
def build_filters():
	filters = []
	ksize = 9
	#define the range for theta and nu
	for theta in np.arange(0, np.pi, np.pi / 8):
		for nu in np.arange(0, 6*np.pi/4 , np.pi / 4):
			kern = cv2.getGaborKernel((ksize, ksize), 1.0, theta, nu, 0.5, 0, ktype=cv2.CV_32F)
			kern /= 1.5*kern.sum()
			filters.append(kern)
	return filters

#function to convolve the image with the filters
def process(img, filters):
	accum = np.zeros_like(img)
	for kern in filters:
		fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
		np.maximum(accum, fimg, accum)
	return accum

if __name__ == '__main__':

	#instantiating the filters
	filters = build_filters()

	f = np.asarray(filters)

	#reading the input image
	imgg = cv2.imread(test,0)
	
	#initializing the feature vector
	feat = []

	#calculating the local energy for each convolved image
	for j in range(40):
		res = process(imgg, f[j])
		temp = 0
		for p in range(128):
			for q in range(128):
				temp = temp + res[p][q]*res[p][q]
		feat.append(temp)
	#calculating the mean amplitude for each convolved image	
	for j in range(40):
		res = process(imgg, f[j])
		temp = 0
		for p in range(128):
			for q in range(128):
				temp = temp + abs(res[p][q])
		feat.append(temp)
 	#feat matrix is the feature vector for the image

