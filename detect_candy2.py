import cv2
import numpy as np

def resize(img, resize_scale: int or float):
    width = int(img.shape[1]*resize_scale)
    hight = int(img.shape[0]*resize_scale)
    dimensions = (width, hight)
    return cv2.resize(img, dimensions)

img = cv2.imread("mnm.jpg")
output = img.copy()
th1 = 90
th2 = 200
count = 0
kernel = np.ones((13, 13), np.uint8)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



canny = cv2.Canny(grayscale, th1, th2)




contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    area = cv2.contourArea(c)
    approx = cv2.approxPolyDP(c, 0.05 * cv2.arcLength(c, True), True)
    
    
    if area>=70:
        pass
    if len(approx)>=3 and area>=60:
        count+=1
        cv2.drawContours(output, [c], 0, (255, 0, 255), 13)
        


cv2.imshow("output", resize(output, 0.3))
print(count)
cv2.waitKey(0)

