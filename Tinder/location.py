from abc import ABC, abstractmethod

class Location:
    def __init__(self, lat: float, lng: float):
        self.__lat = lat
        self.__lng = lng

    def get_distance(self, other: Location):
        return (self.__lat - other.__lat) ** 2 + (self.__lng - other.__lng) ** 2

class LocationService:
    def __init__(self, location_getting_strategy: LocationGettingStrategy):
        self.__location_getting_strategy = location_getting_strategy

    def get_new_location(self):
        return self.__location_getting_strategy.get_new_by_user()

    def set_location_getting_strategy(self, location_getting_strategy: LocationGettingStrategy):
        self.__location_getting_strategy = location_getting_strategy

class LocationGettingStrategy(ABC):
    @abstractmethod
    def get_new_by_user(self):
        raise NotImplementedError("Subclasses must implement this method")

class RandomLocationGettingStrategy(LocationGettingStrategy):
    def get_new_by_user(self):
        return Location(51.507351, -0.127758)

class BasicLocationGettingStrategy(LocationGettingStrategy):
    def get_new_by_user(self):
        return Location(51.507351, -0.127758)