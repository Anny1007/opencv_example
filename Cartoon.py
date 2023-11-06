import cv2
from google.colab.patches import cv2_imshow
# 读取图像
image = cv2.imread('IMG_8229.jpg')


# 1. 将图像模糊
blurred_image = cv2.medianBlur(image, 7)

# 2. 转换为灰度图像
gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

# 3. 检测边缘特征
edges = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 4. 风格化效果，实现卡通效果
color = cv2.bilateralFilter(image, 9, 300, 300)
cartoon_image = cv2.bitwise_and(color, color, mask=edges)

# 保存卡通化后的图像
cv2.imwrite('cartoon_image.jpg', cartoon_image)

# 显示原图和卡通化后的图像
cv2_imshow(image)
cv2_imshow(cartoon_image)
