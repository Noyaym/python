
import cv2
import numpy as np
import argparse
print(0)

def resize(img, resize_scale: int or float):
    width = int(img.shape[1]*resize_scale)
    hight = int(img.shape[0]*resize_scale)
    dimensions = (width, hight)
    return cv2.resize(img, dimensions)




img = cv2.imread("mnm.jpg")
print(0)
output = img.copy()
print(0)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(0)


circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100, minRadius=85, maxRadius=463)
count = 0

print(0)


if circles is not None:
	#circles = np.round(circles[0, :]).astype("int")
    for i in circles[0]:

        print(i)

        (x, y, r) = i

        print(x, y, r)
        x = int(x)
        y = int(y)
        r = int(r)
        cv2.circle(output, (x, y), r, (255, 0, 255), 13)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        count+=1
output = resize(output, 0.2)
cv2.imshow("output", output)
print(count)
cv2.waitKey(0)