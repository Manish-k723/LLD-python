from tv_display import TvDisplay
from weather_station import WeatherStation
from mobile_display import MobileDisplay

ws = WeatherStation()
tv = TvDisplay()
mobile = MobileDisplay()

ws.register_observer(tv)
ws.register_observer(mobile)

ws.update_temp(25)
ws.remove_observer(mobile)
ws.update_temp(55)


