# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:16:40 2021

@author: richa
"""

from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """Parent class for strategy objects"""
    
    allowed_ext = []
    
    @classmethod
    def can_ingest(cls, path: str)->bool:
        """Checks to see if the child strategy object can parse the file type"""
        
        ext = path.split('.')[-1]
        return ext in cls.allowed_ext
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        """Blueprint for parsing method in child straegy objects"""
        
        pass
    