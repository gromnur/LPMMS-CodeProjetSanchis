from ImageCoord import ImageCoord
import os
import sys
import tkinter
from tkinter import filedialog

# Chemin du dossier ou l'on recupere les images
racine = tkinter.Tk()
racine.title("itinPhoto")
racine.directory = filedialog.askdirectory()
cheminDossier = racine.directory
dirImage = os.listdir(cheminDossier)

#création du fichier tampon
os.mkdir('tempMiniature')

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

#Parcours de la liste d'image pour générer les miniatures
for index in range(0,len(listImage)) :
    #icriture de la miniature
    listImage[index]._set_text_JPEGThumbnail(str(index+1))

    #génération de la miniature
    listImage[index]._get_JPEGThumbnail().save("tempMiniature\\"+str(index)+".jpg", "JPEG")


# suppression du fichier tampon
for root, dirs, files in os.walk("tempMiniature"):
   for name in files:
      os.remove("tempMiniature\\"+name)
os.rmdir('tempMiniature')
