# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:06:43 2021

@author: richa
"""

class QuoteModel():
    
    def __init__(self, body, author):
        self.body = body
        self.author = author
    
    def __repr__(self):
        return f'{self.body} - {self.author}'
    
    