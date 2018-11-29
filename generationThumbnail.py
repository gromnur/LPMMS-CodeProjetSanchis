from PIL import Image
import glob, os

size = 128, 128

# Créé une miiature de l'image
im = Image.open("Image/IMG1.jpg")
im.thumbnail(size)
im.save("Image/IMG1thumbnail.png", "PNG")
