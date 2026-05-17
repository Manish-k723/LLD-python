from order import Order

class SaladOrder(Order):
    def __init__(self, chef):
        self._chef = chef

    def cook(self) -> None:
        print("Salad is being prepared")

