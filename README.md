# Computer Vision

<p align="center">
  <img src="https://www.xerox.com/sites/default/files/AOC_Naila_eye_machine.jpg" width="600"/>
</p>

"Humans use their eyes and their brains to see and visually sense the world around them. Computer vision is the science that aims to give a similar, if not better, capability to a machine or computer. Computer vision is concerned with the automatic extraction, analysis and understanding of useful information from a single image or a sequence of images" - that is the definiton google will come up with. It is pretty self explanatory. As the name suggests it gives a sense of intelligence to the vision of the machine i.e the camera.

This is the python implementation of some of the common yet important techniques often used in computer vision. Various methodologies like tracking, marking, contour drawing, feature extraction etc. are explained and implemented.

## Pre Requisites

1. [Thresholding](http://aishack.in/tutorials/thresholding/) 

## Tracking

This method is used when there is a need to track any subject in a video (or a set of frames). A **marker** is drawn around the subject in each frame so as to identify it. The algorithm can be applied on both RGB and HSV colour spaces and the choice really depends upon the situation. 

**RGB** colour space is useful in case of humans. We can generate and identify any colour irrespective of the difference in intensity, texture etc. But machines are not so intelligent to do so. Light blue and dark blue are completely different colours for them. Sometimes, in the RGB colour sapce, there is a difference in the colour across the same surface due to uncontrollable factors. This makes tracking an objeect very difficult.

<p align="center">
  <img src="http://cstwiki.wtb.tue.nl/images/archive/20120520102507%21RGB_HSV.png" width="500"/>
</p>


**HSV** colour space is muxh more efficient when it comes to identifying an object on the basis of its colour. Light blue and dark blue have the same 'Hue' value and hence it is easier to identify the colour in am image in HSV space. Here we present the method in both RGB and HSV colour sapces.

We have *2 datasets* in which we have to **track the red vehicle**. The datasets have not been uploaded on this repository. Please feel free to ask for it.

### RGB Space

In this method the red-green-blue colour channels of the images are used to detect the red vehicle. The code is written from scratch without using any libraries from OpenCV to detect the target. Basic steps followed are:

1. Split the image into blue, green red channels.
2. Subtract the green and blue channels from the red channel. This helps us to retain the pixels where only red colour           is present. For example the white space in the original image contains all the three components. Hence, when green+blue channel is subtracted from the red channel those areas get cancelled which later can be reduced to zero by **thresholding**.
3. Now to place the marker, get the **mean point** among the ones which are not reduced to zero.

### HSV Space

This is an another method which uses hue-saturation-value space to detect the target. This code directly uses various OpenCV libraries for thresholding. Basic steps followed are:

1. Convert the colour space of the image to HSV.
2. Define a range of hue values over which the image will be thresholded. Hue value of any colour can be determined by the inbuilt function of OpenCV **cvtColour**.
3. Now to place the marker, get the **mean point** among the ones which are not reduced to zero.

### Results

#### Dataset 1

Original Image

<p align="center">
  <img src="images/d1_0.jpg" width="500"/>
</p>

Thresholded Image

<p align="center">
  <img src="images/d1_1.png" width="500"/>
</p>

Original image with the marker

<p align="center">
  <img src="images/d1_2.png" width="500"/>
</p>

#### Dataset 2

Original Image

<p align="center">
  <img src="images/d2_0.jpg" width="500"/>
</p>

Thresholded Image

<p align="center">
  <img src="images/d2_2.png" width="500"/>
</p>

Original image with the marker

<p align="center">
  <img src="images/d2_1.png" width="500"/>
</p>
