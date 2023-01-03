
"""
from PIL import Image
from PIL.ExifTags import TAGS

# open the image
image = Image.open("jpg.jpg")

# extracting the exif metadata
exifdata = image.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
	
	# getting the tag name instead of tag id
	tagname = TAGS.get(tagid, tagid)

	# passing the tagid to get its respective value
	value = exifdata.get(tagid)

	# printing the final result
	print(f"{tagname:25}: {value}")
"""

import PIL.Image
import PIL.ExifTags

img = PIL.Image.open('jpg.jpg')
exif_data = img._getexif()
#print(exif_data)


exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    #if k in PIL.ExifTags.TAGS
}

for key in exif:
    print(key)
    print(exif[key])







