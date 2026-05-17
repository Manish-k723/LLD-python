class Chef:
    def cook_pasta(self) -> None:
        print("Cooking pasta")

    def cook_salad(self) -> None:
        print("Cooking salad")

class Waiter:
    def __init__(self, chef: Chef) -> None:
        self._chef = chef

    def place_order(self, item: str) -> None:
        if item == "pasta":
            self._chef.cook_pasta()
        elif item == "salad":
            self._chef.cook_salad()
        else:
            print("Not Available")

chef = Chef()
waiter = Waiter(chef)
waiter.place_order("pasta")

