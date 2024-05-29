import os
import glob
import random
from PIL import Image
from waveshare_epd import epd7in5b_HD
import RPi.GPIO as GPIO


def resize_and_crop(img_path, modified_path, size, crop_type='middle'):
    """
    Resize and crop an image to fit the specified size.

    args:
    img_path: path for the image to resize.
    modified_path: path to store the modified image.
    size: `(width, height)` tuple.
    crop_type: can be 'top', 'middle' or 'bottom', depending on this
    value, the image will cropped getting the 'top/left', 'middle' or
    'bottom/right' of the image to fit the size.
    raises:
    Exception: if can not open the file in img_path of there is problems
    to save the image.
    ValueError: if an invalid `crop_type` is provided.
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    # The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))), Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
            box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0], int(round((img.size[1] + size[1]) / 2)))
        elif crop_type == 'bottom':
            box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else:
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]), Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
            box = (int(round((img.size[0] - size[0]) / 2)), 0, int(round((img.size[0] + size[0]) / 2)), img.size[1])
        elif crop_type == 'bottom':
            box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else:
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else:
        img = img.resize((size[0], size[1]), Image.ANTIALIAS)
    # If the scale is the same, we do not need to crop
    img.save(modified_path)


# Set the photos directory
photos_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'photos/')
images = list(glob.iglob(photos_dir + '/**/*.*', recursive=True))
new_image = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'current.jpg')
print(new_image)


# Pick a photo to show
print("Generating photo")
random_number = random.randint(0, len(images)-1)
resize_and_crop(img_path=images[random_number], modified_path=new_image, size=(880, 528), crop_type="middle")
pil_im = Image.open(new_image)


# Initialise the screen
print("Clear display")
epd = epd7in5b_HD.EPD()
epd.init()  
epd.Clear()

# Show the photo
print("Loading photo")
pil_im = pil_im.convert(mode='1', dither=Image.FLOYDSTEINBERG) # Dither the image into a 1 bit bitmap (Just zeros and ones)
red_image = Image.new('1', (epd.height, epd.width), 255)  # This is blank
epd.display(epd.getbuffer(pil_im), epd.getbuffer(red_image))

# Turn on GPIO pin 18 on. We do this because it allows the photoframe timer to turn off the pi power.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)