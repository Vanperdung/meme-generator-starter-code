"""DocxIngestor.py."""
import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """DocxIngestor class is used to parse quote in docx file."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check suffix of this path."""
        path_list = path.split('.')
        if len(path_list) > 1:
            suffix = path_list[-1]
        else: 
            suffix = ''
        
        return suffix == 'docx'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all quotes in this path."""
        if not cls.can_ingest(path):
            raise ValueError(f'Cant ingest this path {path}')
        
        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():  
                parts = paragraph.text.split(' - ')
                if len(parts) == 2:
                    body, author = parts[0].strip(), parts[1].strip()
                    quote = QuoteModel(body, author)
                    quotes.append(quote)
        return quotes
