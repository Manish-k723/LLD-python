class Position:
    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col

    def get_row(self) -> int:
        return self.__row
    def get_col(self) -> int:
        return self.__col