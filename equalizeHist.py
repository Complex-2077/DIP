import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
image = cv2.imread('./result_image_视网膜.jpg', cv2.IMREAD_GRAYSCALE)

# 直方图均衡化
equalized_image = cv2.equalizeHist(image)

# 显示原图和均衡化后的图像
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(equalized_image, cmap='gray'), plt.title('Equalized Image')
plt.show()

# 保存均衡化后的图像
cv2.imwrite('equalized_image_2.jpg', equalized_image)