import cv2

# 读入图片
image = cv2.imread('./images/gradient_image.jpg')

# 进行均值滤波，核大小为5x5
blurred_image = cv2.blur(image, (5, 5))

# 保存处理后的图片
cv2.imwrite('./images/smooth_gradient_images.jpg', blurred_image)