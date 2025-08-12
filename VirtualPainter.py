import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

script_dir = os.path.dirname(os.path.abspath(__file__))
folderPath = os.path.join(script_dir, "Header")
if not os.path.exists(folderPath):
    raise FileNotFoundError(f"❌ Header folder not found: {folderPath}")


myList=os.listdir(folderPath)
print("Found files:", myList)
print("Total files:", len(myList))

print(myList)
overlayList = []

for imPath in myList:
    image_path = os.path.join(folderPath, imPath)
    image = cv2.imread(image_path)
    
    overlayList.append(image)
print(len(overlayList))

header=overlayList[0]

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


while True:
    success, img = cap.read()
    frame_height, frame_width = img.shape[:2]

    # Resize header to match webcam width, fixed height (e.g. 125 pixels)
    header_height = 125
    header_resized = cv2.resize(header, (frame_width, header_height))

    # Overlay header at top of frame
    img[0:header_height, 0:frame_width] = header_resized

    cv2.imshow("Virtual Painter", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
   

