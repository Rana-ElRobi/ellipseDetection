import cv2
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
		print ("image number : ", count)
		# Read the image
		image = cv2.imread(path + i)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		imgstack.append(image)
		grayStack.append(gray)
		# display last element in the list
		#count = count +1
		#cv2.imshow("Plates found" ,imgstack[-1])
		cv2.waitKey(0)	
	return imgstack , grayStack

# function that applies haough transform ellips on image no 29
# helper link
# http://stackoverflow.com/questions/42206042/ellipse-detection-in-opencv-python	
def detectplates(colorimg , greyimg):
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

def main():
	# load the images
	platesStack , grayPlates = loadPlates()
	# Try Hough transform Elipses on plat no 29
	detectplates(platesStack[29],grayPlates[29])
main()