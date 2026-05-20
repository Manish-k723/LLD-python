from position import Position


class Move:
    def __init__(self, from_position: Position, to_position: Position):
        self._from_position = from_position
        self._to_position = to_position

    def get_from_position(self) -> Position:
        return self._from_position

    def get_to_position(self) -> Position:
        return self._to_position
