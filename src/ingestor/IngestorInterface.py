"""IngestorInterface.py."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """IngestorInterface class is an interface class."""

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Abstract method is used to check suffix of this path."""
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method is used to parse all quotes in this path."""
        pass
