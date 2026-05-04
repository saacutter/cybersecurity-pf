# ==================================================================================================================
# This script was adapted from https://www.geeksforgeeks.org/python/image-based-steganography-using-python/
# ==================================================================================================================

from PIL import Image, ImageFilter, ImageEnhance, ImageOps

PREFIX = "tests/steganography/"

def genData(data):
    """Converts input text into a list of 8-bit binary strings."""
    return [format(ord(i), '08b') for i in data]

def modPix(pix, data):
    """Modifies pixel values to encode the binary data."""
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    
    for i in range(lendata):
        pixels = [value for value in next(imdata)[:3] + next(imdata)[:3] + next(imdata)[:3]]
        
        # Modify pixel values based on binary data
        for j in range(8):
            if datalist[i][j] == '0' and pixels[j] % 2 != 0:
                pixels[j] -= 1
            elif datalist[i][j] == '1' and pixels[j] % 2 == 0:
                pixels[j] = pixels[j] - 1 if pixels[j] != 0 else pixels[j] + 1
        
        # Set termination flag (last pixel even means continue, odd means stop)
        if i == lendata - 1:
            pixels[-1] |= 1  # Make odd (stop flag)
        else:
            pixels[-1] &= ~1  # Make even (continue flag)
        
        yield tuple(pixels[:3])
        yield tuple(pixels[3:6])
        yield tuple(pixels[6:9])

def encode_enc(newimg, data):
    """Encodes the modified pixel data into the new image."""
    w = newimg.size[0]
    (x, y) = (0, 0)
    
    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        x = 0 if x == w - 1 else x + 1
        y += 1 if x == 0 else 0

def encode():
    """Handles user input and calls encoding functions."""
    image = Image.open("base.png", 'r')
    data = "CITS2006PortfolioB30"
    
    newimg = image.copy()
    encode_enc(newimg, data)
    global PREFIX
    newimg.save(PREFIX + "watermarked.png")

def decode(file):
    """Decodes hidden text from an image."""
    image = Image.open(file, 'r')
    imgdata = iter(image.getdata())
    data = ""
    
    while True:
        pixels = [value for value in next(imgdata)[:3] + next(imgdata)[:3] + next(imgdata)[:3]]
        binstr = ''.join(['1' if i % 2 else '0' for i in pixels[:8]])
        data += chr(int(binstr, 2))
        
        if pixels[-1] % 2 != 0:
            break
    
    return data

def filter():
    """Applies the filters to the image."""
    global PREFIX
    image = Image.open(PREFIX + "watermarked.png", 'r')

    image.rotate(90).save(PREFIX + "rotated90.png")
    
    image.rotate(180).save(PREFIX + "rotated180.png")

    image.transpose(Image.FLIP_LEFT_RIGHT).save(PREFIX + "hflip.png")

    image.transpose(Image.FLIP_TOP_BOTTOM).save(PREFIX + "vflip.png")

    image.resize((701, 561)).save(PREFIX + "small.png")

    image.resize((2804, 2244)).save(PREFIX + "big.png")

    ImageOps.crop(image, 1).save(PREFIX + "cropped.png")

    image.convert("L").save(PREFIX + "greyscale.png")

    image.filter(ImageFilter.BLUR).save(PREFIX + "blur.png")

    image.filter(ImageFilter.CONTOUR).save(PREFIX + "contour.png")

    image.filter(ImageFilter.EMBOSS).save(PREFIX + "emboss.png")

    image.filter(ImageFilter.FIND_EDGES).save(PREFIX + "edges.png")

    image.filter(ImageFilter.SHARPEN).save(PREFIX + "sharp.png")

    image.filter(ImageFilter.SMOOTH).save(PREFIX + "smooth.png")

    ImageOps.invert(image).save(PREFIX + "inverted.png")

    ImageEnhance.Brightness(image).enhance(1.5).save(PREFIX + "highbrightness.png")

    ImageEnhance.Brightness(image).enhance(0.5).save(PREFIX + "lowbrightness.png")

    ImageEnhance.Contrast(image).enhance(1.5).save(PREFIX + "highcontrast.png")

    ImageEnhance.Contrast(image).enhance(0.5).save(PREFIX + "lowcontrast.png")

def main():
    """Main function for user interaction."""
    encode()
    filter()

    images = [
        "regenerated.png", "compressed.png", "rotated90.png", "rotated180.png", "hflip.png", "vflip.png", "small.png", "big.png", "cropped.png", "greyscale.png", 
        "blur.png", "contour.png", "emboss.png", "edges.png", "sharp.png", "smooth.png", "inverted.png", "highbrightness.png", "lowbrightness.png", 
        "highcontrast.png", "lowcontrast.png"
    ]
        
    print(f"{'Reference (watermarked.png):':27}", decode(PREFIX + "watermarked.png"))
    for image in images:
        try:
            print(f"{image.split("/")[-1]:>27}: {decode(PREFIX + image)}")
        except:
            print(f"{image.split("/")[-1]:>27}: Decoding failed.")

if __name__ == "__main__":
    main()