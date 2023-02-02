import cv2
import numpy as np


def draw(event, x, y, flags, param):
    # x and y are location of curser in image
    # flag is for which event is done
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 255, 255), 5)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x, y), (x+100, y+100), (255, 255, 255), 2)


cv2.namedWindow(winname="res")

img = np.zeros((512, 512, 3), np.uint8)

cv2.setMouseCallback("res", draw)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) == 27:  # 27 for esc key
        break

cv2.destroyAllWindows()


