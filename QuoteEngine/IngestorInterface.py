# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:16:40 2021

@author: richa
"""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    
    allowed_ext = []
    
    @classmethod
    def can_ingest(cls, path: str)->bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_ext
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str)->List[QuoteModel]:
        pass
    