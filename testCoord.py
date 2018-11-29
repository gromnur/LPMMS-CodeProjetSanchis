from ImageCoord import ImageCoord
import os
import folium
import base64
from io import BytesIO
import copy
import webbrowser

# Chemin du dossier ou l'on recupere les images
cheminDossier = 'Image'
dirImage = os.listdir(cheminDossier)

listImage = []

# Parcour du dossier d'images
for index in range(0,len(dirImage)) :
    img = ImageCoord(cheminDossier + '\\' + dirImage[index])
    listImage.append(img)
    img._set_text_JPEGThumbnail(str(index+1))

    #sauvegarde les miniature
    img._get_JPEGThumbnail().save("Miniature\\"+str(index)+".jpg", "JPEG")

listImage.sort()

# Affich image avec coordonné
#fr a in listImage :
#    if a.has_coord() :
#        print(a.__repr__())

img = listImage[1]
a = (img._get_GPSLatitudeDMS(), img._get_GPSLongitudeDMS())

print("Génération de la carte!")

# Création de la carte
m = folium.Map()

os.mkdir('miniature')

icon = folium.features.CustomIcon('miniature\\0.jpg')

# Ajout d'un marqeur
folium.Marker(location=a, popup='0.jpg', icon=icon).add_to(m)

# Sauvergarde de la carte
m.save("index.html")


#Ouverture de la carte
webbrowser.open("index.html")
