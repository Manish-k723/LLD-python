from payment_status import PaymentStatus


class Payment:
    def __init__(self, payment_id: int, amount: float):
        self._payment_id = payment_id
        self._amount = amount
        self._status = PaymentStatus.PENDING

    def get_payment_id(self) -> int:
        return self._payment_id

    def get_amount(self) -> float:
        return self._amount

    def get_status(self) -> PaymentStatus:
        return self._status

    def mark_paid(self) -> None:
        self._status = PaymentStatus.PAID
