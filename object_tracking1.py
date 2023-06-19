import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

tracker = cv2.TrackerCSRT_create()

returned, img = video,read()

bbox = cv2.selectROI("rastreando", img, False)
tracker.init(img, bbox)

print(bbox)

def draw_box(img, bbox):
    x, y, w, h = int((bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]))
    cv2.rectangle(img, (x,y), ((x+w)), ((y+h)), (255, 0, 255), 3, 1)
    cv2.putText(img, "rastreando", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(O,0,255),2)

while True:
    check,img = video.read()

    success, bbox = tracke.update(img)

    if success:
        draw_box(img, bbox)
    else:
        cv2.putText(img, "Errou", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(O,0,255),2)    

    cv2.imshow("resultado",img)

    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido!")
        break


video.release()
cv2.destroyAllWindows()




