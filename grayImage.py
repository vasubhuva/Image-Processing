import cv2

img = cv2.imread("Images/1296932.png")
img = cv2.resize(img, (1280, 700))
print(img)
cv2.imshow("Real", img)

img = cv2.imread("Images/1296932.png",0)
img = cv2.resize(img, (1280, 700))
print(img)
cv2.imshow("Gray", img)
cv2.waitKey()
cv2.destroyAllWindows()
