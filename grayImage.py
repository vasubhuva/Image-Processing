import cv2

# img = cv2.imread("B:\\sem4\\Image-Processing\\Images\\1296932.png")
# img = cv2.resize(img, (1280, 700))
# print(img)
# cv2.imshow("Real", img)

# giving second parameter 0 will convert image in gray
img = cv2.imread("B:\\sem4\\Image-Processing\\Images\\1296932.png", 0)

img = cv2.resize(img, (1280, 700))
print(img)
cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
