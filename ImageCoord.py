from PIL import Image, ImageDraw, ImageFont
import exifread
import os
import sys
import glob

# Classe image contient les coordonnés GPS ainsi que la miniature de l'image si renseigné
class ImageCoord(object):

    size = 128, 128

    # Renvoi : [%d,%d,%f] à partir d'un String : [%s, %s, %s]
    def conversionTabNombre(GPSTab = "") :
        var = GPSTab.replace("[","").replace("]","").split(", ")
        seconde = list(map(int, var[2].split("/"))) #Conversion en Int
        tab = [int(var[0]),int(var[1]),seconde[0]/seconde[1]]
        return tab

    def __init__(self, cheminImage) :

        # Initialisation variable
        self.CheminImage = cheminImage
        self.Nom = cheminImage.split("\\")[-1]
        self.ImageDateTime = ""
        self.JPEGThumbnail = None
        self.GPSLatitudeRef = ""
        self.GPSLatitude = ""
        self.GPSLongitudeRef = ""
        self.GPSLongitude = ""

        with open(cheminImage,'rb') as image :

            contenu = {}

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
                    contenu[tag] = tags[tag].__str__()

            # Ajout de la date
            if (contenu.__contains__('Image DateTime')) :
                self.ImageDateTime = contenu['Image DateTime']

            # Ajout de la miniature TODO
            ImageCoord._set_JPEGThumbnail(self, self.CheminImage)

            # Met a jour l'image si les coordonné existe
            if (contenu.__contains__('GPS GPSLatitudeRef')) :
                self.GPSLatitudeRef = contenu['GPS GPSLatitudeRef']
            if (contenu.__contains__('GPS GPSLatitude')) :
                self.GPSLatitude = ImageCoord.conversionTabNombre(contenu['GPS GPSLatitude'])
            if (contenu.__contains__('GPS GPSLongitudeRef')) :
                self.GPSLongitudeRef = contenu['GPS GPSLongitudeRef']
            if (contenu.__contains__('GPS GPSLongitude')) :
                self.GPSLongitude = ImageCoord.conversionTabNombre(contenu['GPS GPSLongitude'])


    ## Setter ##
    def _set_Nom(self,Nom):
        self.Nom = Nom

    def _set_ImageDateTime(self,ImageDateTime):
        self.ImageDateTime = ImageDateTime

    def _set_GPSLatitudeRef(self,GPSLatitudeRef):
        self.GPSLatitudeRef = GPSLatitudeRef

    def _set_GPSLatitudeDD(self, GPSLatitude):
        self.GPSLatitude = ImageCoord.conversionTabNombre(GPSLatitude)

    def _set_GPSLongitudeRef(self, GPSLongitudeRef):
        self.GPSLongitudeRef = GPSLongitudeRef

    def _set_GPSLongitudeDD(self, GPSLongitude):
        self.GPSLongitude = ImageCoord.conversionTabNombre(GPSLongitude)

    def _set_JPEGThumbnail(self, lienImage) :
        # Créé une miiature de l'image
        im = Image.open(lienImage)
        im.thumbnail(ImageCoord.size)

        #Eregistrement de l'image
        self.JPEGThumbnail = im

    def _set_text_JPEGThumbnail(self, text = "", position = (2,2), fontSize = 40, font="calibri.ttf") :
        #Police du texte
        font = ImageFont.truetype(font, fontSize)

        # Ecriture sur l'image
        draw = ImageDraw.Draw(self.JPEGThumbnail)
        draw.text(position, text, font=font)


    ## Getter ##

    def _get_Nom(self):
        return self.Nom

    def _get_ImageDateTime(self):
        return self.ImageDateTime

    def _get_GPSLatitudeRef(self):
        return self.GPSLatitudeRef

    def _get_GPSLatitudeDD(self):
        return self.GPSLatitude

    def _get_GPSLongitudeRef(self):
        return self.GPSLongitudeRef

    def _get_GPSLongitudeDD(self):
        return self.GPSLongitude

    def _get_JPEGThumbnail(self):
        return self.JPEGThumbnail

    # Longitude sous la forme DMS
    def _get_GPSLongitudeDMS(self):
        coord = self.GPSLongitude[0] + self.GPSLongitude[1]/60 + self.GPSLongitude[2]/3600
        if self.GPSLongitudeRef == "E" :
            return coord
        if self.GPSLongitudeRef == "O" :
            return -1 * coord
        return None

    # Latitude sous la forme DMS
    def _get_GPSLatitudeDMS(self):
        if ImageCoord.has_coord(self) :
            coord = self.GPSLatitude[0] + self.GPSLatitude[1]/60 + self.GPSLatitude[2]/3600
            if self.GPSLatitudeRef == "N" :
                return coord
            if self.GPSLatitudeRef == "S" :
                return -1 * coord
        else :
            return None

    # Verifie si l'image à des coordonné
    def has_coord(self) :
        return ((self.GPSLatitudeRef != "") &
                (str(self.GPSLatitude) != "") &
                (self.GPSLongitudeRef != "") &
                (str(self.GPSLongitude) != ""))

    # Comparateur permet a la méthode sort de fonctionné correctement
    def __str__(self) :
        return "\n" + self.Nom + ", date:" + self.ImageDateTime + ", lat:" + str(self.GPSLatitude) + ", long:" + str(self.GPSLongitude)

    def __repr__(self) :
        return ImageCoord.__str__(self)

    def __eq__(self,other) :
        return (self.ImageDateTime == other.ImageDateTime)

    def __ne__(self,other) :
        return (self.ImageDateTime != other.ImageDateTime)

    def __lt__(self,other) :
        return (self.ImageDateTime < other.ImageDateTime)
