from payment import Payment


class PaymentService:
    def __init__(self):
        self._next_payment_id = 1

    def pay(self, amount: float) -> Payment:
        payment = Payment(self._next_payment_id, amount)
        payment.mark_paid()
        self._next_payment_id += 1
        return payment
