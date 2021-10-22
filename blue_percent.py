import cv2
import numpy as np
from PIL import Image

## 使用する画像指定 jpgでもpngでも可
img = cv2.imread("./original.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## hsvで抜き出す色の範囲を指定
# mask = cv2.inRange(hsv, (36, 0, 0), (86, 255,255))  #green
# mask = cv2.inRange(hsv, (5, 0, 0), (30, 255,255))  # red
mask = cv2.inRange(hsv, (100, 0, 0), (120, 255, 255))  # blue

imask = mask > 0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

# 黒と青に分けた画像の保存
cv2.imwrite("image.png", green)
img = Image.open('image.png')
black = 0
blue = 0

# 黒とその他の色に分ける
for pixel in img.getdata():

    # rgb値指定
    # if pixel < (1, 1, 1):
    if pixel == (0, 0, 0):
        black += 1
    else:
        blue += 1

print('black=' + str(black) + 'px, blue=' + str(blue) + 'px')
calc_blue = round((blue / (black + blue)), 5)
calc_black = 1 - calc_blue
print("blue(except black)={}% : black={}%".format(calc_blue * 100, calc_black * 100))
