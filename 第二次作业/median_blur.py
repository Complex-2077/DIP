import cv2

# 读入图像
image = cv2.imread('./images/1.png', cv2.IMREAD_GRAYSCALE)

# 检查图像是否成功读入
if image is None:
    print("Error: Could not read image.")
else:
    # 应用中值滤波
    filtered_image = cv2.medianBlur(image, 5)

    # 显示原始图像和滤波后的图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)

    # 等待按键事件并关闭所有窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存滤波后的图像到文件
    cv2.imwrite('./images/median_blur_image.png', filtered_image)