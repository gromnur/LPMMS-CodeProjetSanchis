from ImageCoord import ImageCoord

# Chemin du dossier ou l'on recupere les images
cheminDossier = 'Image'
dirImage = os.listdir(cheminDossier)

listImage = []

# Parcour du dossier d'images
for index in range(0,len(dirImage)) :
    img = ImageCoord(cheminDossier + '\\' + dirImage[index])
    listImage.append(img)

for a in listImage :
    print(a.__repr__())
