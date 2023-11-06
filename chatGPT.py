import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# 读取图像
image = cv2.imread('IMG_8229.png')

# 调整亮度和对比度
alpha = 1.5  # 控制对比度
beta = 50    # 控制亮度
adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# 转换为 HSV 颜色空间
hsv = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2HSV)

# 调整饱和度
saturation = 1.5  # 增加饱和度
hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation, 0, 255)

# 转换回 BGR 颜色空间
enhanced_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 保存美化后的图像
cv2.imwrite('output.jpg', enhanced_image)

# 显示原图和美化后的图像
cv2_imshow(image)
cv2_imshow(enhanced_image)
