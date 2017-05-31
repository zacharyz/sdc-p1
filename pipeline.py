#read image

#convert to grayscale

#define parameters

#define masked edges using a fillPoly


#define hough transform


#run hough on edge detected image
#out is an array containing endpoints of detected line segments

#for each of the lines, draw lines on the blank image


#create the color image

#draw the lines on the edge image

#display the image

def auto_canny(image, sigma=0.33):
   # compute the median of the single channel pixel intensities
   v = np.median(image)
 
   # apply automatic Canny edge detection using the computed median
   lower = int(max(0, (1.0 - sigma) * v))
   upper = int(min(255, (1.0 + sigma) * v))
   edged = cv2.Canny(image, lower, upper)
 
   # return the edged image
   return edged

def pipeline(img):
    
   if type(img) == str:
      image = mpimg.imread(img)
   else:
      image = img

      
   #convert to grayscale
   gray = grayscale(image)

   #apply gaussian blur
   kernal_size = 5
   blur_gray = gaussian_blur(image, kernal_size)

   # Define our parameters for Canny and apply
   # low_threshold = 50
   # high_threshold = 150
   edges = auto_canny(blur_gray)

   #define masked edges using a fillPoly
   imshape = image.shape
   #print("imshape", imshape)

   # vMax = 325

   height = imshape[0]
   width = imshape[1]
   upper_half = height*.6
   ratio = 4/7
   vertices = np.array([[(20,height),((1-ratio)*width, upper_half),(ratio*width, upper_half), (width-20,height)]], dtype=np.int32)
   # vertices = np.array([[(0,imshape[0]),(450, vMax), (520, vMax), (imshape[1],imshape[0])]], dtype=np.int32)
   #print("vertices", vertices)
   masked_edges = region_of_interest(edges, vertices)

   # print("masked edges", masked_edges)

   # Define the Hough transform parameters
   # Make a blank the same size as our image to draw on
   rho = 2 # distance resolution in pixels of the Hough grid
   theta = np.pi/180 # angular resolution in radians of the Hough grid
   threshold = 1     # minimum number of votes (intersections in Hough grid cell)
   min_line_length = 10 #minimum number of pixels making up a line
   max_line_gap = 20    # maximum gap in pixels between connectable line segments
   # line_image = np.copy(image)*0 # creating a blank to draw lines on


   #run hough on edge detected image
   line_image = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)

   # return line_image

   # Create a "color" binary image to combine with line image
   color_edges = np.dstack((edges, edges, edges)) 
   

   #create the color image
   lines_edges = weighted_img(line_image,image) 
   #draw the lines on the edge image
   return lines_edges
    
images = os.listdir("test_images/")
for test_image in images:
   image = pipeline('test_images/'+test_image)
   plt.imshow(image)
   plt.show()