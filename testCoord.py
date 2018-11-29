from ImageCoord import ImageCoord
import os
# Chemin du dossier ou l'on recupere les images
cheminDossier = 'Image'
dirImage = os.listdir(cheminDossier)

listImage = []

# Parcour du dossier d'images
for index in range(0,len(dirImage)) :
    img = ImageCoord(cheminDossier + '\\' + dirImage[index])
    listImage.append(img)
    img._set_text_JPEGThumbnail("1")
    # sauvegarde les miniature
    # img._get_JPEGThumbnail().save("m"+str(index)+".jpg", "JPEG")

# Affich image avec coordonné
for a in listImage :
    if a.has_coord() :
        print(a.__repr__())
