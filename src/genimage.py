from PIL import ImageDraw, ImageFont
import PIL.Image
import json

class TextWriter:
    def __init__(self, font: ImageFont) -> None:
        self.font = font
    def write(self, image, text, position, color = 'black'):
        ImageDraw.Draw(image).text(position, text, fill=color, font=self.font)
        return image

class Text:
    def __init__(self, textstr, textcolor, font):
        self.textstr = textstr
        self.textcolor = textcolor
        self.font = font
    def __repr__(self):
        return f'\n{self.__dict__}'

class Image:
    def __init__(self, title: str, text: list[Text], bgcolor: str):
        self.title = title
        self.text = text
        self.bgcolor = bgcolor
    @staticmethod
    def loadfromjson(jsonfile, fontregistry):
        with open(jsonfile) as f:
            imagesdata = json.load(f)
        for imagedata in imagesdata['images']:
            yield Image(imagedata['title'], [Text(textdata['textstr'], textdata['textcolor'], fontregistry[textdata['font']]) for textdata in imagedata['textlist']], imagedata['bgcolor'])
    
    def draw(self):
        img = PIL.Image.new('RGB', (2500, 2500), color=self.bgcolor)
        twreg = {fontobj:TextWriter(fontobj) for fontstr, fontobj in FONTREGISTRY.items()} # TextWriters for each font in FONTREGISTRY
        for i, text in enumerate(self.text):
            twreg[text.font].write(img, text.textstr, (60, i*160+140), color=text.textcolor)
        return img

    def __repr__(self):
        return f'''\n[{self.__class__} Object:
        title: "{self.title}"
        bgcolor: "{self.bgcolor}"
        text: "{self.text}"]\n'''