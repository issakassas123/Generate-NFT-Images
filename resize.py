from PIL import Image
import os

files = os.listdir(r'old')

for pic in files:
    img = Image.open(rf'old\{pic}')
    img1 = img.resize((700, 700))
    img1.save(rf"new\{pic}", 'png', quality = 100)
