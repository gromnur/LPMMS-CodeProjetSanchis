from ImageCoord import ImageCoord
import os
# Chemin du dossier ou l'on recupere les images
cheminDossier = 'LPMMS-CodeProjetSanchis\Image'
dirImage = os.listdir(cheminDossier)

listImage = []

# Parcour du dossier d'images
for index in range(0,len(dirImage)) :
    img = ImageCoord(cheminDossier + '\\' + dirImage[index])
    listImage.append(img)
    img._set_text_JPEGThumbnail("1")

for a in listImage :
    print(a.__repr__())
