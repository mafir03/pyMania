import cv2 as cv


img = cv.imread("coolcat.jpg")

cv.imshow("image", img)


# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# dilate an image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("eroded", eroded)

# resize
resized = cv.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
