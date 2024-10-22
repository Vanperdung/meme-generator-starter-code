"""CSVIngestor."""
import pandas as pd
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSVIngestor class is used to parse quote in csv file."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check suffix of this path."""
        path_list = path.split('.')
        if len(path_list) > 1:
            suffix = path_list[-1]
        else:
            suffix = ''
        return suffix == 'csv'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all quotes in this path."""
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest this path {path}')

        quotes = []
        df = pd.read_csv(path)
        for row in df.itertuples(index=False):
            quote = QuoteModel(row.body, row.author)
            quotes.append(quote)

        return quotes
