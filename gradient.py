import cv2
import numpy as np

# 读取图像
image = cv2.imread('/Users/complex/Downloads/血管实验数据/IMG/Med-Retina-DRIVE-3.png', cv2.IMREAD_GRAYSCALE)

# 计算梯度
grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# 计算梯度幅值
gradient_magnitude = cv2.magnitude(grad_x, grad_y)

# 归一化梯度图像
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

# 保存梯度图像
cv2.imwrite('./images/gradient_image.jpg', gradient_magnitude)

# # 读取梯度图像
# gradient_image = gradient_magnitude

# # 打印图像大小
# print("Image size:", gradient_image.shape)

# # 应用高斯核卷积平滑噪声
# smoothed_image = cv2.GaussianBlur(gradient_image, (11, 11), 0, borderType=cv2.BORDER_REPLICATE)

# # 保存平滑后的图像
# cv2.imwrite('smoothed_gradient_image_11.jpg', smoothed_image)
