# import the opencv library
from distutils.log import error
from logging import exception
import cv2
import numpy as np


# define a video capture object
vid = cv2.VideoCapture(0)

lower = np.array([94, 87, 82])
upper = np.array([109, 170, 237])

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower, upper)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	try: hierarchy = hierarchy[0]
	except: hierarchy = []
	for contour, hier in zip(contours, hierarchy):
			cv2.drawContours(frame, contour, 0, (0, 0, 255), 3)
			((x,y), r) = cv2.minEnclosingCircle(contour)
			print(x, y, r)
			#cv2.circle(frame, (int(x), int(y)), int(r), (255, 0, 0), 3)
			try:
				r /= 1.1
				pixels = []
				pixels.append(mask[int(y+r), int(x)])
				print("sm1")
				pixels.append(mask[int(y-r), int(x)])
				pixels.append(mask[int(y), int(x-r)])
				pixels.append(mask[int(y), int(x+r)])
				val = True
				print("sm2")
				for p in pixels:
					print(p)
					if (p==0):
						print("nope")
						val = False
				print (val)
				if val:
					print('yay, we entered')
					r *= 1.1
					cv2.circle(frame, (int(x), int(y)), int(r), (0, 255, 0), 3)
					cv2.circle(mask, (int(x), int(y)), int(r), (255, 0, 0), 3)
			except:
				pass

	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
