import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读入图像并指定灰度模式
image = cv2.imread('/Users/complex/Downloads/血管实验数据/IMG/Med-Coronary-ARCADE-5.png', cv2.IMREAD_GRAYSCALE)

# 使用中值滤波降噪
median_blur = cv2.medianBlur(image, 5)

# 使用拉普拉斯算子增强血管
laplacian = cv2.Laplacian(median_blur, cv2.CV_64F)
# enhanced_image = cv2.convertScaleAbs(laplacian)

# 显示结果
plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(132), plt.imshow(median_blur, cmap='gray'), plt.title('Gaussian Blurred Image')
plt.subplot(133), plt.imshow(laplacian, cmap='gray'), plt.title('Enhanced Image')
plt.show()

# 写入文件
# cv2.imwrite('enhanced_image.png', enhanced_image)