# Import Image for basic functionalities like open, save, show
# Import ImageDraw to convert image into editable format
# Import ImageFont to choose the font style

import json

from src.genimage import * # replace *

#TODO: Load fonts automatically by searching paths
# LOAD FONTS
opensansfont = ImageFont.truetype('OpenSans-Regular.ttf', 160)
FONTREGISTRY = {'opensansfont': opensansfont}

images = list(Image.loadfromjson('imgdata.json', FONTREGISTRY))
print(images)

import os
if not os.path.exists('results'):
    os.makedirs('results')

for image in images:
    image.draw().save(f'results/{image.title}.jpeg')