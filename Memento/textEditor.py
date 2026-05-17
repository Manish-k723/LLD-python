from Memento.textMemento import TextMemento

class TextEditor:
    def __init__(self) -> None:
        self._text = ""

    def write(self, new_text: str) -> None:
        self._text += new_text

    def get_text(self) -> str:
        return self._text

    def save(self) -> TextMemento:
        return TextMemento(self._text)

    def restore(self, text_memento: TextMemento) -> None:
        self._text = text_memento.get_text()

