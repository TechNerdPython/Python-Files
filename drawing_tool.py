import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
draw = False
ix = -1
iy = -1

def draw_circle(event, x, y, param, flags):
    global ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            cv2.circle(img, (x, y), 10, (0, 255, 200), -10)
    
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img, (x, y), 10, (0, 255, 200), -10)

cv2.namedWindow('My_Drawing', flags=img)
cv2.setMouseCallback("My_Drawing", draw_circle)

while True:
    cv2.imshow("My_Drawing", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break