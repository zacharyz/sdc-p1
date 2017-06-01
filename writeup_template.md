# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./pipeline/grayscale.png "Grayscale"
[image2]: ./pipeline/gaussian.png "Gaussian"
[image3]: ./pipeline/canny.png "Canny"
[image4]: ./pipeline/maskededges.png "Masked Edges"
[image5]: ./pipeline/houghlines.png "Hough Transform"
[image6]: ./pipeline/finalimage.png "Result"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I .... 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 




#### Convert to Grayscale
![grayscale][image1]

#### Apply Gaussian Blur
![grayscale][image2]
- smooth out features and reduce noise


#### Canny
![canny][image3]
- detect edges within the image


#### Region of Interest
![region][image4]
- limit our area of focus with a region that makes up roughly the bottom 3rd of the image
- defined by a 4 vertice polygon that is bounded by the bottom of the image, and around a vanishing point for the lanes


#### Hough Transform
![houghlines][image5]
- extract line features from the image, and return a list of lines

	

#### Draw Lines
![drawlines][image6]
- from the lines generated find common slopes and use them to extract lines that extend throughout the region
- based on the slope of the lines we can tell if they represent the left or right lane lines.
- eliminate horizontal lines that are not likely to be lane lines that were the result of shadows or other edges (like the vehicle's hood)
- to reduce flickering store previous lines and reuse if no lines are extracted for a given frame.

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...

Shadows
Line twitchiness
Chang

### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...

Auto Canny
Polyfit draw lines
Curved Lines
Dynamic regions