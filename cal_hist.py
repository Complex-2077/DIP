import cv2

import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('result_image.jpg', cv2.IMREAD_GRAYSCALE)

# 检查图像是否成功读取
if image is None:
    print("Error: Could not read image.")
else:
    # 计算直方图
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # 绘制直方图
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()