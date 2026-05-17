import dataclasses

class Location:
    def __init__(self, lat: float, lng: float):
        self.__lat = lat
        self.__lng = lng

    def get_lat(self):
        return self.__lat
    def get_lng(self):
        return self.__lng
    def distance_to(self, other: Location):
        return abs((other.get_lat() - self.get_lat()) + (other.get_lng() - self.get_lng()))
