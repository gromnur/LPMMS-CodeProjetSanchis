import exifread
import os
import sys
from ImageCoord import ImageCoord

if (len(sys.argv) != 2):
	print("syntaxe : python geoLocPhoto.py image")
	sys.exit(1)

image = ImageCoord(sys.argv[1])
print(image.__repr__())
print(image._get_GPSLongitudeDMS())
print(image._get_GPSLatitudeDMS())
