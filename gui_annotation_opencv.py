import cv2
import os
import numpy as np

top_left_corner = []
bottom_right_corner = []

def drawRectangle(action, x,y, flags, *userdata):
    global top_left_corner, bottom_right_corner
    if action == cv2.EVENT_LBUTTONDOWN:

        top_left_corner.append((x,y))
        print(top_left_corner)
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner.append((x,y))
    
        # Draw the rectangle
        cv2.rectangle(img, top_left_corner[-1], bottom_right_corner[-1], (0,255,0),2,8)
        cv2.imshow("Penguin", img)

img = cv2.imread('./sea.jpeg', 1)
img = cv2.resize(img,(0,0), fx=0.4,fy=0.4)
image = img.copy()

cv2.namedWindow("Penguin")
cv2.setMouseCallback("Penguin", drawRectangle)

k = 0
while k!= 113:  # 113 <-> q (Press q to exit)
    cv2.imshow("Penguin", img)
    k = cv2.waitKey(0)
    if k == 99:   # Press c to remove rectangle
        img = image.copy()
        cv2.imshow("Penguin", img)

cv2.destroyAllWindows()
