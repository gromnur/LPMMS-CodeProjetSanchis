from ImageCoord import ImageCoord
import os
import folium
import sys
import webbrowser

# Chemin du dossier ou l'on recupere les images
# cheminDossier = 'D:\\projet python\\LPMMS-CodeProjetSanchis\\Image'
cheminDossier = os.path.abspath(sys.argv[1])
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


print("Génération de la carte!")

centre = (listImage[0]._get_GPSLatitudeDMS(), listImage[0]._get_GPSLongitudeDMS())

# Création de la carte
m = folium.Map(location=centre,zoom_start=8)

#Ajout marqueur carte
for index in range(0,len(listImage)) :
    #Création des icone TODO
    icon = folium.features.CustomIcon("tempMiniature\\"+str(index)+".jpg", icon_size=(70,70))
    coord = (listImage[index]._get_GPSLatitudeDMS(), listImage[index]._get_GPSLongitudeDMS())
    # Ajout d'un marqeur TODO
    folium.Marker(location=coord, popup=listImage[index]._get_Nom(), icon=icon).add_to(m)

# Sauvergarde de la carte
m.save("carte.html")

#Ouverture de la carte
webbrowser.open("carte.html")

# suppression du fichier tampon
for root, dirs, files in os.walk("tempMiniature"):
   for name in files:
      os.remove("tempMiniature\\"+name)
os.rmdir('tempMiniature')
