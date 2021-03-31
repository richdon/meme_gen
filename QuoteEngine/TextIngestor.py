# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:20:32 2021.

@author: richa
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """txt ingestor strategy object."""

    allowed_ext = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses .txt and returns a list of QuoteModel objects."""
        if not cls.can_ingest:
            raise Exception('Cannot ingest file type')

        quotes = []

        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parsed = line.split(' - ')
                parsed = [txt.strip() for txt in parsed]
                quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(quote)

        return quotes
