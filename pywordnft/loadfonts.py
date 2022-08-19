from PIL import ImageFont, _imagingft
from os import getcwd
import glob
import itertools

from .params import DEFAULT_TEXT_SIZE

# LOAD FONTS
cwd = getcwd() # not used
for file in itertools.chain(glob.glob("*.ttf"), glob.glob("*.otf")):
    FONTREGISTRY = {file: ImageFont.FreeTypeFont(file, size=DEFAULT_TEXT_SIZE)}