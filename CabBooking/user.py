import dataclasses

from CabBooking.location import Location


class User:
    def __init__(self, name: str, phone: str, location: Location):
        self.__name = name
        self.__location = location
        self.__phone = phone

    def get_name(self):
        return self.__name
    def get_location(self):
        return self.__location
    def get_phone(self):
        return self.__phone
    def update_location(self, location: Location):
        self.__location = location