import cv2
from PIL import Image
import imagehash

img1=imagehash.average_hash(Image.open("Image-Processing\\OutputImages\\flip3.png"))
img2=imagehash.average_hash(Image.open("Image-Processing\\OutputImages\\flip4.png"))
diff=img1-img2
# print(diff)

# original image and it's gray converted image will be considered as same 
# converted to other colors will be considered as different
if img1==img2:
    print("same")
else:
    print("not")
    print(img1-img2)

if diff==0:
    print("same")
else:
    print("not")
    print(diff)
