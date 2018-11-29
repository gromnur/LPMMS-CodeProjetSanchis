from PIL import Image, ImageDraw, ImageFont
import glob, os

size = 128, 128

# Créé une miiature de l'image
im = Image.open("Image/IMG1.jpg")
im.thumbnail(size)

#Poilice du texte
font = ImageFont.truetype("calibri.ttf", 50)

# Ecriture sur l'image
draw = ImageDraw.Draw(im)
draw.text((2,2), "1",font=font)

# Sauve
im.save("Image/IMG1thumbnail.png", "PNG")s
