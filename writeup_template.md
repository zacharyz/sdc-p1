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
[image4]: ./pipeline/maskeedges.png "Masked Edges"
[image5]: ./pipeline/houghlines.png "Hough Transform"
[image6]: ./pipeline/finalimage.png "Result"
[image7]: ./test_images/solidWhiteCurve.jpg "Initial"
[image8]: ./pipeline/houghlines-nonextrapolated.png "Hough Transform Basic"


---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. 

We first preprocess our image by converting it to grayscale then applying a gaussian blur to it.
The goal of these first two steps is remove non-essential features (noise and color).

Then I apply Canny edge detection to determine the edges our scene.

I think establish a region of interest within the scene to only focus on the lane lines and filter out edges that are not lane lines.

With that image I then apply a Hough Transformation which will detect line segments from the edges established with Canny.

These lines are then applied to the initial image.


### The Image Pipeline:

#### Initial Image
![initial][image7]

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
![houghlines][image8]
- extract line features from the image, and return a list of lines

	

#### Draw Lines
![non-extrapolated][image5]
![drawlines][image6]
- From the lines generated find common slopes and use them to extract lines that extend throughout the region
- Based on the slope of the lines we can tell if they represent the left or right lane lines.
- Additionally we can potentially segregate lines based on what half of the image a point may be in, so if the midpoint of our image is at 450, then we know that everything to the left of it makes up the left lane line and to the right - the right lane line. 
- I eliminate horizontal lines that are not likely to be lane lines that were the result of shadows or other edges (like the vehicle's hood)
- To reduce flickering I store previous line details and reuse them if no lines are extracted for a given frame.

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...

Shadows
Line twitchiness
Changes in line color

### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...

Auto Canny
Polyfit draw lines
Curved Lines
Dynamic regions
Changing in vehicle orientation