class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def enque(self,item):
        self.items.insert(0,item)

    def deque(self):
        return self.items.pop()

    def qsize(self):
        return len(self.items)
    
    def isInside(self, item):
        return (item in self.items)
        

import Image,os
import cv2
from skimage import data, color, img_as_ubyte
# Helper link
def regiongrow(image,epsilon,start_point):

    Q = Queue()
    s = []
    
    x = start_point[0]
    y = start_point[1]
    
    image = image.convert("L")
    Q.enque((x,y))

    
    while not Q.isEmpty():

        t = Q.deque()
        x = t[0]
        y = t[1]
        
        if x < image.size[0]-1 and \
           abs(  image.getpixel( (x + 1 , y) ) - image.getpixel( (x , y) )  ) <= epsilon :

            if not Q.isInside( (x + 1 , y) ) and not (x + 1 , y) in s:
                Q.enque( (x + 1 , y) )

                
        if x > 0 and \
           abs(  image.getpixel( (x - 1 , y) ) - image.getpixel( (x , y) )  ) <= epsilon:

            if not Q.isInside( (x - 1 , y) ) and not (x - 1 , y) in s:
                Q.enque( (x - 1 , y) )

                     
        if y < (image.size[1] - 1) and \
           abs(  image.getpixel( (x , y + 1) ) - image.getpixel( (x , y) )  ) <= epsilon:

            if not Q.isInside( (x, y + 1) ) and not (x , y + 1) in s:
                Q.enque( (x , y + 1) )

                    
        if y > 0 and \
           abs(  image.getpixel( (x , y - 1) ) - image.getpixel( (x , y) )  ) <= epsilon:

            if not Q.isInside( (x , y - 1) ) and not (x , y - 1) in s:
                Q.enque( (x , y - 1) )


        if t not in s:
            s.append( t )

            
    image.load()
    putpixel = image.im.putpixel
    
    for i in range ( image.size[0] ):
        for j in range ( image.size[1] ):
            putpixel( (i , j) , 0 )

    for i in s:
        putpixel(i , 150)
        
    output=raw_input("enter save fle name : ")
    image.thumbnail( (image.size[0] , image.size[1]) , Image.ANTIALIAS )
    image.save(output + ".JPEG" , "JPEG")

def main():
    #load image
    #image_rgb = cv2.imread("coffee.png")
    image_rgb = data.coffee()[0:220, 0:420]
    #image_rgb = colorimg
    print( "Reading image DONE")
    #image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    #image_gray = greyimg
    print("Convert image to greyscale DONE")
    # apply reagion growing
    # Oriantation = 1.6983058850101347
    # startpoint = radious of the ellipes/2 
    # a = 118 , b = 89
    regiongrow(image_rgb,0.5,[118,89])

main()