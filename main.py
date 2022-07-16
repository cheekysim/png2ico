from PIL import Image
import os

psizes = ["16", "24", "32", "48", "64", "96", "128", "256"]
sizes, images = [], []
[images.append(Image.open(str(file))) for file in os.listdir(os.getcwd()) if file.lower().split(".")[0] in psizes]
[sizes.append((int(file.lower().split(".")[0]),int(file.lower().split(".")[0]))) for file in os.listdir(os.getcwd()) if file.lower().split(".")[0] in psizes]
img = Image.open((str(sizes[-1:]).split(",")[0])[2:] + ".png")
img.save('icon.ico', sizes=sizes, append_images=images)