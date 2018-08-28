import cv2
import numpy as np

#在调用划框的时候进行的回调函数
def nothing(x):
    pass

#全局属性
drawing = False
mode = True
ix,iy=0,0
#回调函数
def Draw_Cirle(event,x,y,flags,param):
    s = cv2.getTrackbarPos(switch,'image')
    #根据switch来打开或者关闭开关
    if s==1:
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
    else:
        r=0
        g=0
        b=0

    #全局属性
    global drawing,mode,ix,iy
    #如果触发左键鼠标触发
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True  #开启绘制
        ix, iy = x, y #记录当前的点击点
    elif event == cv2.EVENT_MOUSEMOVE:
        #如果mode其为true，那么绘制颜色不同的矩形
        if drawing ==True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(r,g,b),-1)  #在绘制模式以及是方形绘制模式时候进行绘制
            elif mode == False:
                cv2.circle(img,(x,y),5,(r,g,b),-1)#在绘制模式以及圆形模式的时候开始绘制
    elif event == cv2.EVENT_LBUTTONUP:#当鼠标按键抬起
        drawing=False #停止绘制
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(r,g,b),-1) #开启绘制方形
        elif mode ==False:
            cv2.circle(img,(x,y),5,(r,g,b),-1) #开启绘制圆形

img =np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',Draw_Cirle)
#创建三个框框
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch, 'image', 0,1,nothing)


while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    elif k == ord('m'):
        mode = not mode
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    s=cv2.getTrackbarPos(switch, 'image')

cv2.destroyAllWindows()
