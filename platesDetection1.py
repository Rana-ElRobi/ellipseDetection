import cv2
import matplotlib.pyplot as plt
from skimage import data, color, img_as_ubyte
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter
# load images 
# Returns images loaded in stack and gray version of the image in stack too
def loadPlates():
	#Images main path 
	path= "/home/rana/Desktop/yelp/ellipseDetection/plates/"
	#creat list with images names
	imgnames=[  "76112.jpg" ,"76113.jpg" ,"76121.jpg"  ,
				"76148.jpg" ,"76175.jpg" ,"471517.jpg" ,
				"76162.jpg" ,"76180.jpg" ,"471755.jpg" ,
				"76163.jpg" ,"76189.jpg" ,"471782.jpg" ,
				"471783.jpg" ,"471825.jpg" ,"471864.jpg" ,
				"471792.jpg" ,"471850.jpg" ,"471886.jpg" ,
				"471809.jpg" ,"471861.jpg" ,"471908.jpg" ,
				"471914.jpg" ,"471928.jpg" ,"471954.jpg" ,
				"471916.jpg" ,"471929.jpg" ,"471960.jpg" ,
				"471920.jpg" ,"471939.jpg" ,"471964.jpg" ,
				"471970.jpg" ,"471984.jpg" ,"471988.jpg" ,
				"471971.jpg" ,"471986.jpg" ,"471991.jpg" ,
				"471978.jpg" ,"471987.jpg"]
	#create empty list for images loaded 
	imgstack =[]
	grayStack =[]
	# Loop to load the images in the path 
	count = 0 
	for i in imgnames:
		#print ("image number : ", count)
		# Read the image
		image = cv2.imread(path + i)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		imgstack.append(image)
		grayStack.append(gray)
		# display last element in the list
		count = count +1
		#cv2.imshow("Plates found" ,imgstack[-1])
		#cv2.waitKey(0)	
	return imgstack , grayStack
# Function that applied find countours to find ellipse (TOOOOO SLOW)
# helper link
# http://stackoverflow.com/questions/42206042/ellipse-detection-in-opencv-python	
def detectContoursplates(colorimg , greyimg):
	#--- First obtain the threshold using the greyscale image ---
	ret,th = cv2.threshold(greyimg,127,255, 0)
	#--- Find all the contours in the binary image ---
	_, contours,hierarchy = cv2.findContours(th,2,1)
	cnt = contours
	big_contour = []
	max = 0
	for i in cnt:
		area = cv2.contourArea(i) #--- find the contour having biggest area ---
	   	if(area > max):
	   		max = area
	   		big_contour = i 
	final = cv2.drawContours(colorimg, big_contour, -1, (0,255,0), 3)
	cv2.imshow('final', final)
	return 0
# function that applies haough transform ellips on image no 29
# helper link
# http://scikit-image.org/docs/dev/auto_examples/edges/plot_circular_elliptical_hough_transform.html
def houghTrans(colorimg , greyimg):
	# Load picture, convert to grayscale and detect edges
	#image_rgb = data.coffee()[0:220, 0:420]
	#cv2.imwrite("coffee.png",image_rgb)
	image_rgb = cv2.imread("coffee.png")
	#image_rgb = colorimg
	print( "Reading image DONE")
	image_gray = color.rgb2gray(image_rgb)
	#image_gray = greyimg
	print("Convert image to greyscale DONE")
	print("Finding edges .....")
	edges = canny(image_gray, sigma=2.0,
              low_threshold=0.55, high_threshold=0.8)
	print("Find edges DONE")
	# Perform a Hough Transform
	# The accuracy corresponds to the bin size of a major axis.
	# The value is chosen in order to get a single high accumulator.
	# The threshold eliminates low accumulators
	print ("applying Hough ..........")
	result = hough_ellipse(edges, accuracy=40, threshold=250,
	                       min_size=60, max_size=120)
	result.sort(order='accumulator')
	print ("apply Hough Done")
	# Estimated parameters for the ellipse
	print("Estimating Params ........")
	best = list(result[-1])
	yc, xc, a, b = [int(round(x)) for x in best[1:5]]
	orientation = best[5]
	print("Estimate Params DONE")
	# Draw the ellipse on the original image
	cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
	image_rgb[cy, cx] = (0, 0, 255)
	# Draw the edge (white) and the resulting ellipse (red)
	edges = color.gray2rgb(img_as_ubyte(edges))
	edges[cy, cx] = (250, 0, 0)
	fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4), sharex=True,
	                                sharey=True,
	                                subplot_kw={'adjustable':'box-forced'})
	ax1.set_title('Original picture')
	ax1.imshow(image_rgb)
	ax2.set_title('Edge (white) and result (red)')
	ax2.imshow(edges)
	plt.show()
	#cv2.imwrite("coffee.png",image_rgb)
	cv2.imwrite("plat 29.png",image_rgb)

def main():
	# load the images
	platesStack , grayPlates = loadPlates()
	# Try Contours to find Elipses on plat no 29
	#detectContoursplates(platesStack[29],grayPlates[29])
	# Try Ellips on image coffe
	houghTrans(platesStack[29],grayPlates[29])
	
main()