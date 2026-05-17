class PhoneDisplay:
    def update(self, new_temp: int) -> None:
        print(f"Temperature on Mobile is {new_temp}")

class TvDisplay:
    def update(self, new_temp: int) -> None:
        print(f"Temperature of TV is {new_temp}")

class WeatherStation:
    def __init__(self) -> None:
        self._temp = 0
        self._phone_display = PhoneDisplay()

    def update_temp(self, new_temp: int) -> None:
        self._temp = new_temp
        self.notify_temp()

    def notify_temp(self) -> None:
        self._phone_display.update(self._temp)

WS = WeatherStation()
WS.update_temp(25)
WS.update_temp(20)
