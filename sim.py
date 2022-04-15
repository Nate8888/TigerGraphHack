from venv import create
from PIL import Image, ImageDraw
import numpy as np

width = 1280
height = 720

def create_img():
    img = Image.new('RGB', (width, height), color = 'white')
    
    # Draw a rectangle at (10,10) to (50,50)
    rectangle = ImageDraw.Draw(img)
    rectangle.rectangle((10,10,50,50), fill = 'black', outline = 'red')
    img.show()

create_img()