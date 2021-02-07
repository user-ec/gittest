import cv2
import matplotlib.pyplot as plt

for i in range(1,98):
    img = cv2.imread('D:\\webtoonimg\\601-800\\img ({}).png'.format(i),0)
    maxval = 255
    thresh = 126
    blocksize = 15
    c = 20
    th02 = cv2.adaptiveThreshold(img, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, c)
    cv2.imwrite('D:\\webtoonimg\\{}.png'.format(i+600),th02)
