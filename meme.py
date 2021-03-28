# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:13:59 2021

@author: richa
"""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():        
    """class to build a meme"""
    
    def __init__(self, save_path):
        """Initialize with an output path"""
        
        self.save_path = save_path
        

    def resize(self, path:str, size:int) -> str:
        """Resize the image in path dependent on width entered
        in size variable"""
        
        try:
            im = Image.open(path)
            
        except FileNotFoundError:  
            print('The file was not opened')
        
        im.thumbnail(size)
        im.save(f"{self.save_path}/resized.jpg")       
    
        return f"{self.save_path}/resized.jpg"
    
    
    def write_text(self, path, body, author):
        """Open the resized image and write text on the image"""
        
        tmp = random.randint(2000, 3000)
        im = Image.open(f"{self.save_path}/resized.jpg")
        x, y = 10, 10
        pointsize = 22
        fillcolor = 'white'
        shadowcolor = 'black'        
        font_path = './fonts/impact.ttf'
        
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(font_path, pointsize)
        text = body +' - ' + author
        
        # thicker border
        draw.text((x-1, y-1), text, font=font, fill=shadowcolor)
        draw.text((x+1, y-1), text, font=font, fill=shadowcolor)
        draw.text((x-1, y+1), text, font=font, fill=shadowcolor)
        draw.text((x+1, y+1), text, font=font, fill=shadowcolor)
        
        draw.text((x, y), text, font = font, fill = fillcolor, align='center')
        im.save(f"{self.save_path}/{tmp}.jpg")
        
        return f"{self.save_path}/{tmp}.jpg"
        
    
    def make_meme(self, path, body, author, width = 500):
        """Build a meme using the helper methods"""
        
        height = width
        size = (width, height)
        
        meme_path = self.write_text(self.resize(path, size), body, author)
        
        return meme_path
