from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: int):
        ...

class CreditCard(PaymentMethod):
    def pay(self, amount: int):
        print(f"Processing credit card payment {amount}")

class Paypal(PaymentMethod):
    def pay(self, amount: int):
        print(f"Processing paypal payment {amount}")

class BankTransfer(PaymentMethod):
    def pay(self, amount: int):
        print(f"Processing bank transfer payment {amount}")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: int):
        self.payment_method.pay(amount)

credit = CreditCard()
paypal = Paypal()
payment_processor = PaymentProcessor(credit)
payment_processor.process_payment(100)
payment_processor.payment_method = paypal
payment_processor.process_payment(200)
