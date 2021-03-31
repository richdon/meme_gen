# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:06:43 2021.

@author: richa
"""


class QuoteModel():
    """Class for building quote objects."""

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Print the body and author of quote."""
        return f'{self.body}\n - {self.author}'
