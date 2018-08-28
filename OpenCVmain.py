import numpy as np
import cv2

#第二个参数是如何去读取这个图片
#cv2.IMREAD_COLOR:读取一副彩色图片，不包含alpha
#cv2.IMREAD_GRAYSCALE:以灰度模式读取图像
#cv2.IMREAD_UNCHANGED:读入一副图像，包括图像的alpha
img = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)

#用于设置新的窗口，从而达到对窗口缩放的效果
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#窗口显示图像
cv2.imshow("image", img)
#键盘绑定函数，如果在特定秒数内，如果按下任意键
#那么就返回值为-1，如果我们设置该函数的参数为0
#那么就会无限期等待键盘输入
k = cv2.waitKey(0)
if k ==27:
    # 轻易删除各种窗口
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("miku.png",img)
    cv2.destroyAllWindows()  #保存图像

