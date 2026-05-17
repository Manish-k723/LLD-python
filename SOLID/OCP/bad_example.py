class PaymentProcessor:
    def pay(self, payment_method: str, amount: int):
        if payment_method == "credit_card":
            print(f"Processing credit card payment{amount}")
        elif payment_method == "paypal":
            print("Processing paypal payment")
        elif payment_method == "bank_transfer":
            print("Processing bank transfer payment")

payment_processor = PaymentProcessor()
payment_processor.pay("credit_card", 100)

""" what If I have add not a new payment method, then I need to modify the code 
which violates the open-closed principle
"""