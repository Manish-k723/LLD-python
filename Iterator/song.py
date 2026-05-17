class Song:
    def __init__(self, name: str, artist: str):
        self.__name = name
        self.__artist = artist

    def get_name(self) -> str:
        return self.__name
    def get_artist(self) -> str:
        return self.__artist