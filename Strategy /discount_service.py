from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def process_payment(self) -> str:
        return self._strategy.get_discount()

    def set_strategy(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

