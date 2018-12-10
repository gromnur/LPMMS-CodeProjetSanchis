from ImageCoord import ImageCoord
import os
import sys
from folium.features import DivIcon

# Chemin du dossier ou l'on recupere les images

racine = tkinter.Tk()
racine.title("listPhoto")
racine.directory = filedialog.askdirectory()
cheminDossier = racine.directory
dirImage = os.listdir(cheminDossier)

listImage = []

# Parcour du dossier d'images
for index in range(0,len(dirImage)) :
    #parcours du dossier
    img = ImageCoord(cheminDossier + '\\' + dirImage[index])

    #Insertion des image avec coordonné
    if img.has_coord() :
        listImage.append(img)

# Tri des images
listImage.sort()
