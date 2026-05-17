class TextMemento:
    def __init__(self, text: str) -> None:
        self._saved_text = text

    def get_text(self) -> str:
        return self._saved_text
