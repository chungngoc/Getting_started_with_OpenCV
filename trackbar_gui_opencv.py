import cv2

max_scale_up = 100
scaleFactor = 0
window_name = "Resize_Image"
trackbar_value = "Scale"

img = cv2.imread('./sea.jpeg', 1)
img = cv2.resize(img,(0,0), fx=0.4, fy=0.4)
# Create a window to display results
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

def scaleImage(*args):
    # Get the scale factor from the trackbar
    scaleFactor = 1 - args[0]/100.0
    # Resize the image
    scaledImage = cv2.resize(img, (0,0), fx=scaleFactor, fy = scaleFactor)
    cv2.imshow(window_name, scaledImage)

cv2.createTrackbar(trackbar_value, window_name, scaleFactor, max_scale_up, scaleImage)

# Display
cv2.imshow(window_name, img)
c = cv2.waitKey(0)
cv2.destroyAllWindows()



