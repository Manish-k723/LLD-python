from observer import Display

class MobileDisplay(Display):
    def update(self, temp: int) -> None:
        print(f"Mobile Display Updated {temp}")