from PIL import Image
import os

psizes = ["16", "24", "32", "48", "64", "96", "128", "256"]
images = [Image.open(str(file)) for file in os.listdir(os.getcwd()) if file.lower().split(".")[0] in psizes]
sizes = [int(file.lower().split(".")[0]) for file in os.listdir(os.getcwd()) if file.lower().split(".")[0] in psizes]
sizes.sort()
sizes = [(size, size) for size in sizes]
tsizes = [str(file.split(".")[0]) for file in os.listdir(os.getcwd()) if file.lower().split(".")[0] in psizes]
msizes = [size for size in psizes if size not in tsizes]
convert = "n"
if msizes:
    convert = input("You are missing the following size(s):\n" + ", ".join(msizes) + "\nWould you like to add them | Y / N\n")
if convert.lower() == "y":
    tsizes = [(16, 16), (24, 24), (32, 32), (64, 64), (96, 96), (128, 128), (256, 256)]
    for size in msizes:
        img = Image.open((str(sizes[-1:]).split(",")[0])[2:] + ".png")
        tsize = (int(size), int(size))
        img = img.resize((tsize), resample=2) 
        img.save(f'{size}.png')
    images = [Image.open(str(file)) for file in os.listdir(os.getcwd()) if file.lower().split(".")[0] in psizes]
    img = Image.open("256.png")
    img.save('icon.ico', sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (96, 96), (128, 128), (256, 256)], append_images=images)
else:
    img = Image.open((str(sizes[-1:]).split(",")[0])[2:] + ".png")
    print((str(sizes[-1:]).split(",")[0])[2:] + ".png")
    img.save('icon.ico', sizes=sizes, append_images=images)