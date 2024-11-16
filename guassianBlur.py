import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读入图像并指定灰度模式
image = cv2.imread('/Users/complex/Downloads/血管实验数据/IMG/Med-Coronary-ARCADE-5.png', cv2.IMREAD_GRAYSCALE)

# 使用高斯卷积降噪
kernel_size = 13
sigma = 2  # 你可以指定标准差
gaussian_blur = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma, borderType=cv2.BORDER_REPLICATE)

# 显示结果
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(gaussian_blur, cmap='gray'), plt.title('Gaussian Blurred Image')
plt.show()

# 写入文件
cv2.imwrite(f'guassian_blured_{kernel_size}.png', gaussian_blur)