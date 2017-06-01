# **Finding Lane Lines on the Road** 

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
[image7]: ./pipeline/initial.png "Initial"
[image8]: ./pipeline/houghlines-nonextrapolated.png "Hough Transform Basic"


---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. 

I first preprocess the initial image by converting it to grayscale then applying a gaussian blur to it.

The goal of these first two steps is remove non-essential features such as noise and color.

Then I apply Canny edge detection to determine the edges the scene.

I then establish a region of interest within the scene to only focus on the lane lines and filter out edges that are not lane lines.

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
- From the lines generated I find the average slopes of lines segments and use them to generate lines that extend throughout the region (bounded by the min and max extent of our lines and region)
- Based on the sign of the slope (positive or negative) of the lines I can tell if they represent the left or right lane lines.
- Additionally I can potentially segregate lines based on what half of the image a point may be in, so if the midpoint of our image is at 450, then we know that everything to the left of it makes up the left lane line and to the right - the right lane line. 
- I eliminate horizontal lines based on their slopes that are not likely to be lane lines that were the result of shadows or other edges (like the vehicle's hood)
- To reduce flickering I store previous line details and reuse them if no lines are extracted for a given frame.

### 2. Identify potential shortcomings with your current pipeline

#### Shadows, weather and lighting changes.
These all have the potential to change the visual appearance of our lines and will change the criteria that we are using to select them.

Where I live in Portland the lane lines are notorious for blending in with the street when the roads are wet (which as you can imagine happens a lot).

#### Distance from other vehicles and vehicle orientation.
I make the assumption that the vanishing point of our region will be constant (the upper boundary of my region for detection). But if get closer to a car then the extents of our region will change based on the distance to the vehicle or other objects that may be in our path. Additionally what I assume to be "horizontal" can change if the vehicle isn't parallel with the lane.


### 3. Suggest possible improvements to your pipeline

Some possible improvements:

#### Auto Canny and Better Hough Transform Parameters
I made an implementation of canny which does not rely on predefined or tweaked thresholds but instead uses the median pixel intensity of the image and creates thesholds based on that. In theory this produces accurate edges, in practice though I found it occasionally produced results that weren't ideal for parameters that I had established for my hough transform. So alternatively I could rely on auto canny and create hough parameters that work better with it.

#### Polyfit draw lines
I also experimented with an implementation of draw_lines that uses Polyfit. This is called draw_lines_polyfit. This implementation filters points based on where they are in the scene. Then using numpy's polyfit; computes the slope and intersect of the right and left lines based on the filtered points.

#### Curved Lines
I don't currently represent lanes that are curved well. I apply a line that fits the curve but more severe curves would not match a strictly linear line.

#### Futher flickering reduction and line stability
I account for the detection of no lines by displaying a previous result, but I don't account well for what results in a twitchiness of my lines. I could potentially resolve this by limiting the changes in slopes of my lines on a frame per frame basis or interpolating between them. 