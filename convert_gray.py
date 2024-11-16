from PIL import Image

# 读入图片
image = Image.open('/Users/complex/Downloads/血管实验数据/IMG/Med-Retina-DRIVE-3.png')

# 转换为灰度图片
gray_image = image.convert('L')

# 保存灰度图片
gray_image.save('output_image.jpg')