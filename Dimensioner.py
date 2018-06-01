
from PIL import Image
latestdimensions = (3000, 4000)

im = Image.open("PhotoNameWithExtension") 

photobreadth, photobreadth = im.size
dim = photobreadth / float(photobreadth)
endlength = int(latestdimensions[0] / dim)      



if endlength < 1200:
    endbreadth = latestdimensions[0]
    endlength = endlength
else:
    endbreadth = int(dim * latestdimensions[1])
    endlength = latestdimensions[1]

#Dimensioning of image
imaged = im.resize((endbreadth, endlength), Image.ANTIALIAS) 

imaged.show()       #To show image
imaged.save("OutputPhotoName", quality=100) #Image saved on disk
