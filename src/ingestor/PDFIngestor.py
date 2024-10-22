"""PDFIngestor.py."""
import PyPDF2
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import subprocess
import tempfile
import os


class PDFIngestor(IngestorInterface):
    """PDFIngestor class is used to parse quote in PDF file."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check suffix of this path."""
        path_list = path.split('.')
        if len(path_list) > 1:
            suffix = path_list[-1]
        else:
            suffix = ''

        return suffix == 'pdf'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all quotes in this path."""
        if not cls.can_ingest(path):
            raise ValueError(f'Cant ingest this path {path}')

        quotes = []

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
                temp_path = temp_file.name

            subprocess.run(['pdftotext', path, temp_path], check=True)
            with open(temp_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(' - ')
                        if len(parts) == 2:
                            body, author = parts[0].strip(), parts[1].strip()
                            quote = QuoteModel(body, author)
                            quotes.append(quote)
        except subprocess.CalledProcessError as error:
            raise Exception(f"Error when calling pdftotext: {error}")

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

        return quotes
