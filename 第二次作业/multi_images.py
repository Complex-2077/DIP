import cv2
import numpy as np

# 读入两个图像
image1 = cv2.imread('./images/laplacian_image_8.png')
image2 = cv2.imread('./images/smooth_gradient_images.jpg')

# 确保两个图像的尺寸相同
if image1.shape != image2.shape:
    raise ValueError("图像尺寸不匹配")

# 图像相乘
result = cv2.multiply(image1, image2)

# 显示结果
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 将结果写回文件
cv2.imwrite('./images/template.png', result)