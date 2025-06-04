from PIL import Image
import os

# 转换 PNG 为 ICO
png_path = r"C:\Users\12548\Pictures\夸克\47f8fd4bcdc53c777dcb24d8baa207c7_720.png"
ico_path = os.path.join(os.getcwd(), "assets", "app_icon.ico")

# 创建 assets 目录
os.makedirs("assets", exist_ok=True)

# 转换并保存
img = Image.open(png_path)
img.save(ico_path, format='ICO', sizes=[(256,256), (64,64), (32,32)])

print(f"图标已保存到: {ico_path}")