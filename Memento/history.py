from Memento.textMemento import TextMemento


class History:
    def __init__(self):
        self._history: list[TextMemento] = []
        self._redo_history: list[TextMemento] = []

    def save_state(self, text_memento: TextMemento) -> None:
        self._history.append(text_memento)
        self._redo_history = []

    def undo(self) -> TextMemento:
        if self._history:
            text = self._history.pop()
            self._redo_history.append(text)
            if self._history:
                return self._history[-1]
        return TextMemento("")

    def redo(self) -> TextMemento:
        if self._redo_history:
            text = self._redo_history.pop()
            self._history.append(text)
            return text
        return TextMemento("")

    def get_history(self):
        for i in range(len(self._history)):
            print(self._history[i].get_text())

    def get_redo_history(self):
        for i in range(len(self._redo_history)):
            print(self._redo_history[i].get_text())