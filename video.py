##동영상 프레임 추출
##로그(SRT)가 있으면 먼저 읽어서, 중복도를 계산해서 거리에 따라 프레임 간격을 추출하는 알고리즘이 목표

import cv2
import os

print(cv2.__version__)

filepath = './data/2023/DJI_0006.MP4'
video = cv2.VideoCapture(filepath)

if not video.isOpened():
    print("Could not Open :", filepath)
    exit(0)
else:
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

print("frame_count :", frame_count)
print("width :", width)
print("height :", height)
print("fps :", fps)

for i in range(frame_count):
    ret, frame = video.read()

    progress = (i/frame_count)*100

    print("progress: ", progress)

    # print("ret: ", ret)
    # print("frame_count:", i)
    
    if (ret and (i%60==0)):
        image_path = f"./data/2023/images/{i}.jpg"
        cv2.imwrite(image_path, frame)

print("Completed")
video.release()

