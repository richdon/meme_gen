# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:13:59 2021

@author: richa
"""
from PIL import Image, ImageDraw, ImageFont
import random
import pathlib

# Globals for img path
here = pathlib.Path('.')
tmp_dir = here.absolute() / 'tmp'


class MemeEngine():
        
    @classmethod
    def resize(cls, path, size):
        
        try:
            im = Image.open(path)
        except FileNotFoundError:  
            print('The file was not opened')
        
        im.thumbnail(size)
        im.save(f"{tmp_dir}/resized.jpg")       
    
        return f"{tmp_dir}/resized.jpg"
    
    @classmethod
    def write_text(cls, path, body, author):
        
        tmp = random.randint(2000, 3000)
        
        try:
            im1 = Image.open(f"{tmp_dir}/resized.jpg")
        except FileNotFoundError:  
            print('The file was not opened')
        
        draw = ImageDraw.Draw(im1)
        font = ImageFont.truetype("arial.ttf", 18)
        phrase = body +' - ' + author
        draw.text((60, 350), phrase, font = font, fill = 'white')
        im1.save(f"{tmp_dir}/{tmp}.jpg")
        
        return f"{tmp_dir}\{tmp}.jpg"
        
    @classmethod
    def MakeMeme(cls, path, body, author, width = 500):
        
        height = width
        size = (width, height)
        
        meme_path = cls.write_text(cls.resize(path, size), body, author)
        
        return meme_path