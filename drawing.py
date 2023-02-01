import numpy as np
import cv2

img=cv2.imread("Image-Processing\\Images\\1296932.png")
img = cv2.resize(img, (1280, 700))

# img=np.zeros([1000,1200,3],np.uint8)*255 #for black image

# img=np.ones([900,1500,3],np.uint8)*255 #for white image

# line function parameters(img,start,end,color,thickness) 
# color in BGR format
img=cv2.line(img,(0,0),(200,200),(192,192,192),3)

# arrowedline same as line function
img=cv2.arrowedLine(img,(0,0),(100,200),(192,192,192),3)

# rectangle ame as line
# value of thickness in minus will fill the shape
img=cv2.rectangle(img,(300,300),(100,550),(192,192,192),4)

# circle parameters(img,start,radius,color,thickness)
# value of thickness in minus will fill the shape
img=cv2.circle(img,(498,400),30,(192,192,192),3)

# add text in image
font =cv2.FONT_ITALIC # variable to store the type of font
# puttext function parameters(img,text,start,font,fontsize,color,thickness,linetype)
img=cv2.putText(img,"Hello World!",(900,500),font,2,(192,192,192),4,cv2.LINE_AA)

# elipse parameters(img,start,(length,height),color,thickness)
img=cv2.ellipse(img,(700,650),(50,50),0,0,180,192,5)
# 0,0 is uded for rotation
# 180 is used for degree of elipse
# 192 is color code



cv2.imshow("x",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
