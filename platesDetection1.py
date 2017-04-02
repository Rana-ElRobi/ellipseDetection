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

def detectplates():
	return 0

def main():
	# load the images
	platesStack , grayPlates = loadPlates()
	# Try Hough transform Elipses on plat no 29

main()