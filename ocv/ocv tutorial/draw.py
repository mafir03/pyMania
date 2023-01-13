import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

img = cv.imread("coolcat.jpg")

# paint image a certain color
# blank[:] = 0, 255, 0

# draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow("rectangle", blank)

# draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow("circle", blank)

# draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow("line", blank)

# write a text
cv.putText(img, 'Cool Cat', (img.shape[1]//2, img.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)

cv.imshow("image", img)

cv.waitKey(0)
