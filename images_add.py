from PIL import Image, ImageChops

# 打开两个图像
image1 = Image.open('/Users/complex/Downloads/血管实验数据/IMG/Med-Retina-DRIVE-3.png').convert('L')
image2 = Image.open('./images/template.png').convert('L')

# 确保两个图像的尺寸相同
image1 = image1.resize((min(image1.size[0], image2.size[0]), min(image1.size[1], image2.size[1])))
image2 = image2.resize((min(image1.size[0], image2.size[0]), min(image1.size[1], image2.size[1])))

# 将两个图像相加，并夹断高于255的值为255
result_image = ImageChops.add(image1, image2, scale=1.0, offset=0)

# 保存结果图像
result_image.save('result_image_视网膜.jpg')