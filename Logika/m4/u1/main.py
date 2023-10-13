from PIL import Image, ImageFilter

with Image.open('cat.jfif') as original:
    print(original.size)
    print(original.format)
    print(original.mode)

    print(original.info)

    bw_original = original.convert('L')
    bw_original.show()
    blur_original = original.filter(ImageFilter.BLUR)
    blur_original.show()

    left_original = original.transpose(Image.ROTATE_90)
    left_original.show()


    def blur()