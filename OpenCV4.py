import numpy as np
import cv2
#这里给当前一张图进行赋值
img = np.zeros((512,512,3),np.uint8)
#这里绘制一条线，起点+终点+颜色+厚度
cv2.line(img,(0,0),(511,511),(255,0,0),5)
#绘制一个方形，起点+终点+颜色+厚度
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#绘制一个圆形，中点+半径+颜色+厚度，其中设置为-1进行填充
cv2.circle(img,(447,63), 63,(0,0,255),6)
#绘制一个椭圆，中点+长宽+旋转角度+绘制角度大小+颜色+厚度
cv2.ellipse(img,(256,256),(100,50),0,0,360,(0,255,255),-1)
#绘制多边形：首先设置对应点集，其次开始绘制整个的图形
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255))
#绘制文字:文字+位置+字体+大小+颜色+粗细+线条类型
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'FUCK',(10,500),font,
            3,(255,255,255),13,cv2.LINE_AA)
#所有绘图函数返回的都为None

cv2.imshow("line", img)
cv2.waitKey(0)