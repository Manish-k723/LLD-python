from observer import Display
from typing import List

class WeatherStation:
    def __init__(self) -> None:
        self._temp: int = 0
        self._observers: List[Display] = []

    def register_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def update_temp(self, new_temp: int) -> None:
        self._temp = new_temp
        self.notify_observers()

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temp)