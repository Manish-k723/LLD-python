class Player:
    def __init__(self, player_id: int, name: str, is_white: bool) -> None:
        self.__id = player_id
        self.__name = name
        self.__is_white = is_white

    def get_id(self) -> int:
        return self.__id
    def get_name(self) -> str:
        return self.__name
    def get_is_white(self) -> bool:
        return self.__is_white