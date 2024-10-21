import PyPDF2
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        path_list = path.split('.')
        if len(path_list) > 1:
            suffix = path_list[-1]
        else: 
            suffix = ''
        
        return suffix == 'pdf'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f'Cant ingest this path {path}')
        
        quotes = []
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text().strip()
                lines = page_text.split('\n')
                for line in lines:
                    line = line.strip()
                    if line:
                        parts = line.split(' - ')
                        if len(parts) == 2:
                            body, author = parts[0].strip(), parts[1].strip()
                            quote = QuoteModel(body, author)
                            quotes.append(quote)
        return quotes
