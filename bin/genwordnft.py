#!/usr/bin/env python -i

import json

from pywordnft.genimage import * # replace *

images = list(Image.loadfromjson('imgdata.json'))
print(images)

import os
if not os.path.exists('results'):
    os.makedirs('results')

for image in images:
    image.draw().save(f'results/{image.title}.jpeg')