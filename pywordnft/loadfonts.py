from PIL import ImageFont, _imagingft
from os import getcwd
import glob
import itertools

# LOAD FONTS
cwd = getcwd() # not used
for file in itertools.chain(glob.glob("*.ttf"), glob.glob("*.otf")):
    FONTREGISTRY = {file: ImageFont.FreeTypeFont(file, size=160)} # add to not overwrite