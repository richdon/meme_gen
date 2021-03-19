# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:18:41 2021

@author: richa
"""
from QuoteEngine import PDFIngestor, TextIngestor, CSVIngestor, DocxIngestor, Ingestor

print(Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))

