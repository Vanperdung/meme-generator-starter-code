"""TextIngestor.py."""
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """TextIngestor class is used to parse quote in txt file."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check suffix of this path."""
        path_list = path.split('.')
        if len(path_list) > 1:
            suffix = path_list[-1]
        else: 
            suffix = ''
        
        return suffix == 'txt'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all quotes in this path."""
        if not cls.can_ingest(path):
            raise ValueError(f'Cant ingest this path {path}')
        
        quotes = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line = line.strip()
                if line:
                    parts = line.split(' - ')
                    if len(parts) == 2:
                        body, author = parts[0].strip(), parts[1].strip()
                        quote = QuoteModel(body, author)
                        quotes.append(quote)
        return quotes
