import cv2
import matplotlib.pyplot as plt
# image = cv2.imread('./framecap/frames1136.png')
# #
# # for i, col in enumerate(['b', 'g', 'r']):
# #     hist = cv2.calcHist([image], [i], None, [256], [0, 256])
# #     plt.plot(hist, color=col)
# #     plt.xlim([0, 256])
#
# red = cv2.calcHist([image], [2], None, [256], [0, 256])
# plt.plot(red, color='red')
# plt.xlim([0, 256])
# print(red)
# print(sum(red[-5:-1]))
# plt.show()

counter = int(1)
def histo():
    global counter
    image = cv2.imread(f'./test/{counter}.png')
    for i, col in enumerate(['b', 'g', 'r']):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        if sum(hist[-1]) > 50:
            print(col,counter,  hist[-1])

for _ in range(16):
    histo()
    counter+= 1