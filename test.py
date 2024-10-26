from PIL import Image

# 打开原始图像
input_image_path = r'C:/Users/刘志强\Desktop/favicon.png'  # 替换为你的输入图像路径
output_image_path = r'C:/Users/刘志强/Desktop/output_image.png'  # 输出图像路径

# 打开图像并调整大小
with Image.open(input_image_path) as img:
    # 调整图像大小
    resized_img = img.resize((35, 25))
    
    # 保存为PNG格式
    resized_img.save(output_image_path, format='PNG')

print(f"图像已成功转换并保存为 {output_image_path}")
