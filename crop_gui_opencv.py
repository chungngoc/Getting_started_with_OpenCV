import cv2
import os
import numpy as np

top_left_corner = []
bottom_right_corner = []

img = cv2.imread('./content/sea.jpeg', 1)
img = cv2.resize(img,(0,0), fx=0.4,fy=0.4)
image = img.copy()
cropped_image = image.copy()

def cropImage(action, x,y, flags, *userdata):
    global top_left_corner, bottom_right_corner
    global cropped_image

    if action == cv2.EVENT_LBUTTONDOWN:
        top_left_corner.append((x,y))
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner.append((x,y))
    
        cropped_image = img[top_left_corner[-1][1] : bottom_right_corner[-1][1], top_left_corner[-1][0] : bottom_right_corner[-1][0]]
        cv2.imshow("Penguin", img)
        cv2.imshow("Cropped", cropped_image)

cv2.namedWindow("Penguin")
cv2.setMouseCallback("Penguin", cropImage)

k = 0
count = 0
path = "./content/cropped"
while k!= 113:  # 113 <-> q (Press q to exit)
    cv2.imshow("Penguin", img)
    k = cv2.waitKey(0)
    if k == 115:   # Press s to save
        count +=1
        file_name = "penguin_cropped_" + str(count) + ".png"
        cv2.imwrite(os.path.join(path, file_name), cropped_image)

cv2.destroyAllWindows()