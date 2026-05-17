from Command.order import Order

class Waiter:
    def take_order(self, order: Order) -> None:
        order.cook()

