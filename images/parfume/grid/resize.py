import PIL
from PIL import Image

PIL.Image.MAX_IMAGE_PIXELS = 933120000
mywidth = 1200

for imname in ['podacha.jpg']:
	img = Image.open(imname)
	wpercent = (mywidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
	img.save(imname)

