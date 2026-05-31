from __future__ import annotations


class Location:
    def __init__(self, lat: float, lng: float):
        self._lat = lat
        self._lng = lng

    def distance_to(self, other: Location) -> float:
        return ((self._lat - other._lat) ** 2 + (self._lng - other._lng) ** 2) ** 0.5

