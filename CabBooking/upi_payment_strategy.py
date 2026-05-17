from payment_strategy import PaymentStrategy

class UpiPaymentStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using UPI")