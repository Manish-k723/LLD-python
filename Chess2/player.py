from color import Color


class Player:
    def __init__(self, player_id: int, name: str, color: Color):
        self._player_id = player_id
        self._name = name
        self._color = color

    def get_id(self) -> int:
        return self._player_id

    def get_name(self) -> str:
        return self._name

    def get_color(self) -> Color:
        return self._color
