import cv2
# load images 
# Returns images loaded in stack and gray version of the image in stack too
def loadPlates():
	#Images main path 
	path= "/home/rana/Desktop/yelp/100Sample/people/"
	#creat list with images names
	imgnames=[  "408830.jpg" ,"409268.jpg" ,"469954.jpg"  ,
				"470265.jpg" ,"470580.jpg" ,"470804.jpg" ,
				"470294.jpg" ,"470647.jpg" ,"470822.jpg" ,
				"470408.jpg" ,"470662.jpg" ,"470894.jpg" ,
				"470953.jpg" ,"471344.jpg" ,"471271.jpg" ,
				"471073.jpg" ,"471463.jpg" ,"471279.jpg" ,
				"471103.jpg" ,"471550.jpg" ,"471333.jpg" ,
				"471671.jpg" ,"471753.jpg" ,"471797.jpg" ,
				"471800.jpg" ]
	#create empty list for images loaded 
	imgstack =[]
	grayStack =[]
	# Loop to load the images in the path  
	for i in imgnames:
		# Read the image
		image = cv2.imread(path + i)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		imgstack.append(image)
		grayStack.append(gray)
		# display last element in the list
		print (i)
		cv2.imshow("Faces found" ,imgstack[-1])
		cv2.waitKey(0)	
	return imgstack , grayStack

def detectplates():
	return 0

def main():
	# load the images
	platesStack , grayPlates = loadPlates()

main()