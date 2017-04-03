# ellipseDetection
This repo targets detection of plates from set of images from yelp competition dataset
# 1st Trial (Hough transform ellipse detection )
(on cup of coffee image)
# NB
This script gets great results on image of cup of coffee only , other images takes soo long time but i didnt reach results yet from other images.

edge detection params:

sigma=2.0
low_threshold=0.55
high_threshold=0.8

Hough ellipse parrams:

accuracy=40, 
threshold=250,
min_size=60, 
max_size=120

# PlatesDetction.py 
- is the main file that load the images and apply hough trnasform ellipes detection
# regiongrow.py
- is trial for region growing but didnt work
# regiongrow2.py
- is another trial for region growing but its results is very poor
