from song import Song
from playlist import Playlist
from linked_list_playlist import LinkedListPlaylist

song1 = Song("Song1", "Artist1")
song2 = Song("Song2", "Artist2")
song3 = Song("Song3", "Artist3")
song4 = Song("Song4", "Artist4")

playlist = Playlist()
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)
playlist.add_song(song4)

# iterator = playlist.create_iterator()
# while iterator.has_next():
#     print(iterator.next().get_name())

linked_list_playlist = LinkedListPlaylist()
linked_list_playlist.add_song(song1)
linked_list_playlist.add_song(song2)
linked_list_playlist.add_song(song3)
linked_list_playlist.add_song(song4)

iterator = linked_list_playlist.create_iterator()
while iterator.has_next():
    print(iterator.next().get_name())
