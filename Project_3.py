#I DID NOT INCLUDE A VIDEO on purpose :). I'm taking the class P/NP and have two midterms Wed!

def standardize_image_size(img):
    '''takes an input image and returns a new image with the same
    color cropped to 1000x1000 pixels.
    Tags: PARTIAL_MODIFICATION '''
    result = Image.new("RGB", (1000, 1000))
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if x < 1000 and y < 1000:
                color = img.getpixel((x, y)) 
                result.putpixel((x, y), color)
    return result

def apply_filter_to_image(img):
    '''iterates through each pixel in the image and 
    multiplies the red, green, and blue values in each pixel
    Tags: FILTER '''
    width, height = img.size
    for x in range(width):
        for y in range(height):
            color = img.getpixel((x, y))
            r, g, b = color
            img.putpixel((x, y), (r*4, g*2, b*3))
    return img

def overlay_images(img1, img2):
    '''Resizes the two input images to 1000x1000 pixels and then
    overlays the two images by averaging the color values at each pixel.
    Tags: COPY_BLEND'''
    one = img1.resize((1000, 1000))
    two = img2.resize((1000, 1000))
    width, height = one.size
    for x in range(width):
        for y in range(height):
            r1, g1, b1 = one.getpixel((x, y))
            r2, g2, b2 = two.getpixel((x, y))
            r = (r1 + 2*r2) // 2
            g = (g1 + 2*g2) // 2
            b = (b1 + 2*b2) // 2
            one.putpixel((x, y), (r, g, b))
    return one


def arrange_images(img1, img2, img3):
    '''Creates a new image with dimensions 2000x2000 pixels and
    copies the input images into the new image. 2 in the top half of the image
    and 1 centered in the bottom half. 
    Tags: PARTIAL_MODIFICATION, COPY_BLEND'''
    new = Image.new("RGB", (2000,2000))
    width, height = new.size
    for x in range(width//2):
        for y in range(height//2):
            color1 = img1.getpixel((x, y))
            new.putpixel((x, y), color1)
    
    for x in range(161, 1839):
        for y in range (1000, height):
            color2 = img2.getpixel((x-161,y-1000))
            new.putpixel((x,y), color2)
    for x in range(1000, width):
        for y in range (1000):
            color3 = img3.getpixel((x-1000, y))
            new.putpixel((x,y), color3)
    new.show()



from PIL import Image
Image1 = Image.open("CSE 8A Homework/CSE 8A Projects/CSE8A_Project3.py/mushroom_1.jpeg")
Image2 = Image.open("CSE 8A Homework/CSE 8A Projects/CSE8A_Project3.py/mushroom_2.jpeg")
Image3 = Image.open("CSE 8A Homework/CSE 8A Projects/CSE8A_Project3.py/mushroom_3.jpeg")
Image4 = Image.open("CSE 8A Homework/CSE 8A Projects/CSE8A_Project3.py/mushroom_4.jpeg")

#modifying the images
newimg1 = standardize_image_size(Image3)
newimg2 = apply_filter_to_image(Image2)
newimg3 = overlay_images(Image3, Image4)

#passing the modified images to the final function
arrange_images(newimg1, newimg2, newimg3)

