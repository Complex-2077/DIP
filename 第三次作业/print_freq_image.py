import cv2
import numpy as np

import matplotlib.pyplot as plt

# 读取图像
image_path = './car-moire-pattern.tif'
image = cv2.imread(image_path, 0)

# 进行傅立叶变换
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# 显示频谱图
plt.figure(figsize=(10, 10))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.axis('off')

# 保存频谱图到文件
spectrum_path = 'magnitude_spectrum.png'
plt.savefig(spectrum_path)
plt.show()
