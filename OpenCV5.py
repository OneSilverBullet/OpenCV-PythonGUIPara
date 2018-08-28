import cv2
import numpy as np

def draw_circle(event, x,y, flags,param):
    #如果鼠标单击一下，那么就开始绘制图形
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
#将鼠标事件进行注册
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow("image",img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()