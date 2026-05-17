from observer import Display

class TvDisplay(Display):
    def update(self, temp: int) -> None:
        print(f"TV Display Updated {temp}")