import numpy as np
import cv2
from matplotlib import pyplot as plt

#读入相关的图像
img = cv2.imread("1.jpg",cv2.IMREAD_UNCHANGED)
#使用plt进行图片显示
plt.imshow(img, cmap='gray', interpolation='bicubic')
#隐藏对应的plt的横纵坐标
plt.xticks([]),plt.yticks([])
plt.show()