import cv2 as cv


def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)


def rescaleFrame(frame, scale=0.75):
    # works for video, image, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(r"C:\Users\ACER\Downloads\ariandel.mp4")

while True:
    isTrue, frame = capture.read()

    frameResized = rescaleFrame(frame)
    cv.imshow('Video', frameResized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
