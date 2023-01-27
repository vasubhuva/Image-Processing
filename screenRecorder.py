import cv2 as c
import pyautogui as p

# Create Resolutions
rs = p.size()

# filename in which we store recording
fn = input("Enter Any File Name And Path : ")
# fix the frame rate
fps = 30.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn, fourcc, fps, rs)
