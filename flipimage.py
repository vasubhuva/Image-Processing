import cv2

img1=cv2.imread("B:\\sem4\\Image-Processing\\Images\\1296932.png")
img1=cv2.resize(img1,(1000,700))\
    
# we can pass 0,1,-1 as second parameter it will change the direction of image
img1=cv2.flip(img1,0) 
# img1=cv2.flip(img1,1)
# img1=cv2.flip(img1,-1)

img1=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
cv2.imshow("image",img1)
# Just for checking purpose
# cv2.waitKey(0)
# cv2.destroyAllWindows()

k=cv2.waitKey(0)

if k==ord("s"):
    cv2.imwrite("B:\\sem4\\Image-Processing\\OutputImages\\flip.png",img1)
else:
    cv2.destroyAllWindows()
