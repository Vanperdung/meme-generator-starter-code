"""Ingestor.py."""
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Ingestor class is used to parse quote in all files."""

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all quotes in this path."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f'No suitable ingestor found for {path}')
