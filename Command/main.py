from Command.waiter import Waiter
from chef import Chef
from pizze_order import PizzaOrder
from salad_order import SaladOrder

chef = Chef()
pizza_order = PizzaOrder(chef)
salad_order = SaladOrder(chef)

waiter = Waiter()
waiter.take_order(pizza_order)
waiter.take_order(salad_order)

