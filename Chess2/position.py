class Position:
    def __init__(self, row: int, col: int):
        self._row = row
        self._col = col

    def get_row(self) -> int:
        return self._row

    def get_col(self) -> int:
        return self._col

    def __eq__(self, other) -> bool:
        return isinstance(other, Position) and self._row == other._row and self._col == other._col
