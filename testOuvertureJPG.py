import exifread
import os
import sys
from ImageCoord import ImageCoord

listImage = []

# Chemin du dossier ou l'on recupere les images
cheminDossier = 'Image'
dirImage = os.listdir(cheminDossier)

# Ouverture d'un fichier log
fsorti = open('testlog.txt','w')
# Parcour du dossier d'images
for index in range(0,len(dirImage)) :

    # Table des données recupéré par photo
    contenu = {}

    # Ouverture d'une image
    with open(cheminDossier + '\\' + dirImage[index],'rb') as image :
        # Séparation dans le fichier
        print ("\n\nImage " + str(index) + ":\n" ,file = fsorti)

        #Ouverture du EXIF de l'image JPG
        tags = exifread.process_file(image)

        #Parcour des tag EXIF de l'image JPG ouverte précédament
        for tag in tags.keys():
            # On garde les tag souhaité
            if tag in ('GPS GPSLatitudeRef',
                       'GPS GPSLatitude',
                       'GPS GPSLongitudeRef',
                       'GPS GPSLongitude',
                       'Image DateTime') :
                print ("Key: %s, value %s" % (tag, tags[tag]), file=fsorti)
                contenu[tag] = tags[tag].__str__()
        #Créé une image avec son nom
        anImage = ImageCoord(Nom = dirImage[index])

        # Ajoute la miniature
        if (contenu.__contains__('Image DateTime')) :
            anImage._set_ImageDateTime(contenu['Image DateTime'])

        # Met a jour l'image si les coordonné existe
        if (contenu.__contains__('GPS GPSLatitudeRef')) :
            anImage._set_GPSLatitudeRef(contenu['GPS GPSLatitudeRef'])
        if (contenu.__contains__('GPS GPSLatitude')) :
            anImage._set_GPSLatitudeDD(contenu['GPS GPSLatitude'])
        if (contenu.__contains__('GPS GPSLongitudeRef')) :
            anImage._set_GPSLongitudeRef(contenu['GPS GPSLongitudeRef'])
        if (contenu.__contains__('GPS GPSLongitude')) :
            anImage._set_GPSLongitudeDD(contenu['GPS GPSLongitude'])

        listImage.append(anImage)

# Tri les image par ordre chronologique
listImage.sort()

# Affiche quels image ont des coordonné
for img in listImage :
    print(img.has_coord())

print(listImage[0].__repr__())

a = [listImage[0]._get_GPSLatitudeDMS(),listImage[0]._get_GPSLongitudeDMS()]
print(a)
