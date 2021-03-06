from ImageCoord import ImageCoord
import os
import sys
import folium
import webbrowser
import tkinter
from tkinter import filedialog
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

print("Génération de la carte!")

centre = (listImage[0]._get_GPSLatitudeDMS(), listImage[0]._get_GPSLongitudeDMS())

# Création de la carte
m = folium.Map(location=centre,zoom_start=8)

#Ajout marqueur carte
for index in range(0,len(listImage)) :
    coord = (listImage[index]._get_GPSLatitudeDMS(), listImage[index]._get_GPSLongitudeDMS())
    # Ajout d'un marqeur TODO
    folium.Marker(location=coord, popup=listImage[index]._get_Nom(), icon=DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<div style="font-size: 17pt">'+listImage[index]._get_Nom()+'</div>',)).add_to(m)

# Sauvergarde de la carte
m.save("carte.html")

#Ouverture de la carte
webbrowser.open("carte.html")
