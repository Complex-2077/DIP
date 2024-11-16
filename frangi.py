import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from skimage.filters import frangi

# 读取图像并转换为浮点格式
image = img_as_float(io.imread('/Users/complex/Downloads/血管实验数据/IMG/Med-Coronary-ARCADE-3.png', as_gray=True))

# 应用Frangi血管增强滤波器
frangi_image = frangi(image, scale_range=(1, 10), scale_step=2)

# 将增强后的图像转换为8位格式
frangi_image_8bit = (frangi_image * 255).astype(np.uint8)

# 保存增强后的图像
# io.imsave('frangi.png', frangi_image_8bit)

# 显示原图和增强后的图像
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(image, cmap="gray")
ax[0].set_title("Original Image")
ax[0].axis("off")

ax[1].imshow(frangi_image, cmap="gray")
ax[1].set_title("Frangi Enhanced Image")
ax[1].axis("off")

plt.show()