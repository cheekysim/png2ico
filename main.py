from PIL import Image
import os

psizes = ["16", "24", "32", "48", "64", "96", "128", "255"]
sizes, images = [], []
[images.append(file) for file in os.listdir(os.getcwd()) if file.lower().split(".")[0] in psizes]
[sizes.append((int(size.split('.')[0]),int(size.split('.')[0]))) for size in images]
img = Image.open(str(images[-1:])[2:-2])
img.save('icon.ico', sizes=sizes)