"""QuoteModel.py."""


class QuoteModel:
    """QuoteModel is a format class of quote."""

    def __init__(self, body: str, author: str):
        """Initialize the QuoteModel."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return quote."""
        return f'"{self.body}" - {self.author}'
