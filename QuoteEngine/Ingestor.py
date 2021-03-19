# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:54:00 2021

@author: richa
"""
import argparse

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor 
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor

class Ingestor(IngestorInterface):
    
    importers = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path:str)->List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
            
            
            
if __name__ == "__main__":
    cli_parser = argparse.ArgumentParser(description='Generate Meme')
    cli_parser.add_argument('path', type=str,
                        help='file path to quote and author') 
    
    args = cli_parser.parse_args()
    
    print(Ingestor.parse(f'{args.parse}'))