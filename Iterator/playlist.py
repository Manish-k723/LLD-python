from list_iterator import ListIterator


class Playlist:
    def __init__(self):
        self.__songs = []

    def add_song(self, song):
        self.__songs.append(song)

    def create_iterator(self):
        return ListIterator(self.__songs)
