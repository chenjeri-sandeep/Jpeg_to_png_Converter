import sys
import os
from PIL import Image

Img_folder = sys.argv[1]
output_folder = sys.argv[2]
print(Img_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(Img_folder):
    img = Image.open(f"{Img_folder}{file_name}")
    clean_name = os.path.splitext(file_name)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done !!")
