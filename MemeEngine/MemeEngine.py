# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:13:59 2021

@author: richa
"""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():        
    
    def __init__(self, save_path):
        
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
        
        tmp = random.randint(2000, 3000)
        
        try:
            im1 = Image.open(f"{self.save_path}/resized.jpg")
        except FileNotFoundError:  
            print('The file was not opened')
        
        draw = ImageDraw.Draw(im1)
        font = ImageFont.truetype("arial.ttf", 18)
        phrase = body +' - ' + author
        draw.text((0, 0), phrase, font = font, fill = 'white', align='center')
        im1.save(f"{self.save_path}/{tmp}.jpg")
        
        return f"{self.save_path}/{tmp}.jpg"
        
    
    def make_meme(self, path, body, author, width = 500):
        
        height = width
        size = (width, height)
        
        meme_path = self.write_text(self.resize(path, size), body, author)
        
        return meme_path