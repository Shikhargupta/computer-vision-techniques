# Computer Vision

## Introduction
"Humans use their eyes and their brains to see and visually sense the world around them. Computer vision is the science that aims to give a similar, if not better, capability to a machine or computer. Computer vision is concerned with the automatic extraction, analysis and understanding of useful information from a single image or a sequence of images" - that is the definiton google will come up with. It is pretty self explanatory. As the name suggests it gives a sense of intelligence to the vision of the machine i.e the camera.

This is the python implementation of some of the common yet important techniques often used in computer vision. Various methodologies like thresholding, tracking, marking, contour drawing, feature extraction etc. are explained and implemented.

## Tracking

This method is used when there is a need to track any subject in a video (or a set of frames). A **marker** is drawn around the subject in each frame so as to identify it. The algorithm can be applied on both RGB and HSV colour spaces and the choice really depends upon the situation. 

**RGB** colour space is useful in case of humans. We can generate and identify any colour irrespective of the difference in intensity, texture etc. But machines are not so intelligent to do so. Light blue and dark blue are completely different colours for them. Sometimes, in the RGB colour sapce, there is a difference in the colour across the same surface due to uncontrollable factors. This makes tracking an objeect very difficult.

**HSV** colour space is muxh more efficient when it comes to identifying an object on the basis of its colour. Light blue and dark blue have the same 'Hue' value and hence it is easier to identify the colour in am image in HSV space. Here we present the method in both RGB and HSV colour sapces.

We have *2 datasets* in which we have to track the red vehicle. The datasets have not been uploaded on this repository. Please feel free to ask for it.

### RGB Space

