# Import Image for basic functionalities like open, save, show
# Import ImageDraw to convert image into editable format
# Import ImageFont to choose the font style
from PIL import Image, ImageDraw, ImageFont

class TextWriter:
    def __init__(self, font):
        self.font = font
    def write(self, image, text, position, color = 'black'):
        ImageDraw.Draw(image).text(position, text, fill=color, font=self.font)
        return image

class Text:
    def __init__(self, textstr, textcolor, font):
        self.textstr = textstr
        self.textcolor = textcolor
        self.font = font

class ImageData:
    def __init__(self, text: Text, bgcolor):
        self.text = text
        self.bgcolor = bgcolor

# Font selection from the downloaded file
opensansfont = ImageFont.truetype('OpenSans-Regular.ttf', 160)
 
img = Image.new('RGB', (2500, 2500), color='white')

tw = TextWriter(opensansfont)
textlist = ['red hat', 'mustache', 'gold chain']
for i, text in enumerate(textlist):
    tw.write(img, text, (60, i*160+140))
 
# show and save the image
img.show()