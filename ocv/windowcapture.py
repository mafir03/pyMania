import win32gui
import win32ui
import win32con
import numpy as np
import cv2 as cv
import pyautogui
import time

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005

class WindowCapture:

    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0


    def __init__(self, window_name):

        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)



def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)


def hist(screenshot):
    histB = cv.calcHist([screenshot[750:850, 800:900]], [0], None, [256], [0, 256])
    histG = cv.calcHist([screenshot[750:850, 800:900]], [1], None, [256], [0, 256])
    histR = cv.calcHist([screenshot[750:850, 800:900]], [2], None, [256], [0, 256])
    if sum(histG[-1]) > 200:
        pyautogui.keyDown('r')
        pyautogui.keyUp('r')
    if sum(histR[-1]) > 200:
        pyautogui.keyDown('r')
        if sum(histB[-1] < 200):
            pyautogui.keyUp('r')
def main():
    global wincap
    loop_time = time.time()
    while True:
        screenshot = wincap.get_screenshot()
        cv.imshow('Computer Vision', screenshot[750:850, 800:900])
        hist(screenshot)
        # cv.imwrite(f'./framecap/frames{frame}.png', screenshot[750:900, 800:900])

        # print('FPS {}'.format(1 / (time.time() - loop_time)))
        # loop_time = time.time()

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


if __name__ == '__main__':
    wincap = WindowCapture('Osu!')
    main()


"""
Problem with this build
While windows capture itself is fast, the execution of keys itself is slows down entire program.

Also, pressing down key isn't actually pressing down key, which is problematic


"""