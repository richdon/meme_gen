# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:08:45 2021

@author: richa
"""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """PDF ingestor strategy object"""
    
    allowed_ext = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses PDF and returns a .txt and
        then parses the txt to a list of QuoteModel objects"""
        
        if not cls.can_ingest(path):
            raise Exception('cannot ingest file type')
        
        tmp = f'./{random.randint(0,10000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        
        file_ref = open(tmp, "r")
        quotes = []
        
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(quote)
        
        file_ref.close()
        os.remove(tmp)
        return quotes