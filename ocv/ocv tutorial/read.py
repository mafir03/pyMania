import cv2 as cv


# img = cv.imread("prototype.png")

# cv.imshow("image", img)

# cv.waitKey(0)


capture = cv.VideoCapture(r"C:\Users\ACER\Downloads\ariandel.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()


