# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:34:09 2021

@author: richa
"""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSV ingestor strategy object"""
    
    allowed_ext = ['csv']
    
    @classmethod
    def parse(cls, path: str)->List[QuoteModel]:
        """Parses CSV and returns a list of QuoteModel objects"""
        
        if not cls.can_ingest:
            raise Exception('Cannot ingest file type') 
       
        quotes = []      
        df = pd.read_csv(path, header = 0)
            
        for index, row in df.iterrows():
            quote = QuoteModel(row[0], row[1])
            quotes.append(quote)
            
        return quotes
