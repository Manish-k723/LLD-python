from CabBooking.payment_strategy import PaymentStrategy


class PaymentService:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.__payment_strategy = payment_strategy

    def pay(self, amount):
        self.__payment_strategy.pay(amount)

    def refund(self, amount):
        print(f"Refunding {amount}")