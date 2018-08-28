import numpy as np
import cv2
#使用摄像序列读取对应视频的每一帧图片
cap = cv2.VideoCapture('monster.mp4')
while(True):
    #cap.read函数返回一个布尔值（True/False）如果读取正确，那么为true
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow('frame',gray)
    #这里设置waiteKey的值越大，视频播放越慢
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()