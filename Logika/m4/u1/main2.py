from PIL import Image, ImageFilter
class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.edited = []

    def open(self):
        try:
            self.original = Image.open(self. filename)
            self.original.show()
        except:
            print('не існує')


    def do_left(self):
        left = self.original.transpose(Image.ROTATE_90)
        self.edited.append(left)

        left.save('left_' + self.filename)
    
    def bw(self):
        bw = self.original.convert('L') 
        self.edited.append(bw)

        bw.save('bw_' + self.filename)

img = ImageEditor('left_cat.jfif')  


img.open()
img.do_left()
img.bw()