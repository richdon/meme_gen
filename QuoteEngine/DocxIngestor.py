# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:27:33 2021.

@author: richa
"""
from docx import Document
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """DOCX ingestor strategy object."""

    allowed_ext = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses DOCX and returns a list of QuoteModel objects."""
        if not cls.can_ingest:
            raise Exception('Cannot ingest file type')

        quotes = []
        doc = Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                parsed = [txt.strip() for txt in parsed]
                quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(quote)

        return quotes
