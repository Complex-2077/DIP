import cv2
import numpy as np

# 读入图像
image = cv2.imread('/Users/complex/Downloads/血管实验数据/IMG/Med-Retina-DRIVE-3.png', cv2.IMREAD_GRAYSCALE)

# 定义拉普拉斯核
kernel = np.array([[-1, -1, -1], 
                   [-1,  8, -1], 
                   [-1, -1, -1]])

# 应用拉普拉斯核进行卷积
laplacian = cv2.filter2D(image, -1, kernel, borderType=cv2.BORDER_REPLICATE)

# 保存拉普拉斯图像到文件
cv2.imwrite('./images/laplacian_image_8.png', laplacian)