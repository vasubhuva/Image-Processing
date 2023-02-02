import cv2
import datetime

cap = cv2.VideoCapture("Image-Processing\\Videos\\onzanimez.mp4")

print("Width=", cap.get(3))  # 3 is for width
print("Height=", cap.get(4))  # 4 is for height

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 600))
    if ret == True:
        font = cv2.FONT_ITALIC
        text = 'height:'+str(cap.get(4))+'width:'+str(cap.get(3))
        frame = cv2.putText(frame, text, (100, 100), font,
                            1, (0, 0, 0), 1, cv2.LINE_AA)
        date_data = "Date="+str(datetime.datetime.now())
        frame = cv2.putText(frame, date_data, (25, 25), font,
                            1, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.circle(frame, (498, 400), 30, (192, 192, 192), 3)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
