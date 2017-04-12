from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw
from django.utils.six import BytesIO
import os

def download_image(request, text):

    # Path configurations
    image_app_path = os.path.dirname(__file__)

    font_path = os.path.join(image_app_path, 'UnPilgia.ttf')

    # image_path => not used
    # image_path = os.path.join(image_app_path, 'image_archive/'+text+'.jpg')

    # Image size
    im_width, im_height = 256, 256

    # Set font
    font = ImageFont.truetype(font_path, 50)

    # Create blank image
    with Image.new('RGB', size=(im_width, im_height), color='white') as img:

        # Construct ImageDraw.Draw on Image created above
        draw = ImageDraw.Draw(img)

        # Text size
        text_width, text_height = font.getsize(text)

        # Align Image
        text_location = (im_width - text_width)/2, (im_height - text_height)/2

        # Draw text
        draw.text(text_location, text, font=font, fill='black')

        # # Save Image
        # img.save(image_path)

        io = BytesIO()
        img.save(io, format='PNG')
        io.seek(0)

        # Render Image
        return HttpResponse(io, content_type='image/png')

        # with open(image_path, 'rb') as f:
        #     return HttpResponse(io, content_type='image/jpeg')
