from email.mime import image
import cv2
import numpy as np

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

img = cv2.imread("mnm.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask0 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

mask = mask0+ mask1

canny = cv2.Canny(img, 100, 200)

cc=0


contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
count = 0
for c in contours:
    try:
        cv2.drawContours(img, c, 0, (0, 0, 255), 3)
        cc+=1
        ((x,y), r) = cv2.minEnclosingCircle(c)
        r /=1.1
        pixels = []
        pixels.append(mask[int(y+r), int(x)])
        pixels.append(mask[int(y-r), int(x)])
        pixels.append(mask[int(y), int(x-r)])
        pixels.append(mask[int(y), int(x+r)])
        val = True
        for p in pixels:
            if (p==0):
                val = False
        if val:
            r*=1.1
            print(x, y, r)
            cv2.circle(img, (int(x), int(y)), int(r), (0, 0, 0), 10)
            count+=1

    except:
        pass


#rows, cols, _ = img.shape
#for i in range(rows):
  #  for j in range(cols):
 #       k = canny[i, j]
 #       if k==255:
          #  img[i, j] = (153, 171, 71)


    

def resize(img, resize_scale: int or float):
    width = int(img.shape[1]*resize_scale)
    hight = int(img.shape[0]*resize_scale)
    dimensions = (width, hight)
    return cv2.resize(img, dimensions)
print(cc, "cc")
img = resize(img, 0.3)
canny = resize(canny, 0.2)
cv2.imshow("candy", img)
cv2.imshow("canny", canny)
print(count)
cv2.waitKey(0)
