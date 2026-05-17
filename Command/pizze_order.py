from order import Order

class PizzaOrder(Order):
    def __init__(self, chef):
        self._chef = chef

    def cook(self):
        print("Pizza is being prepared")

