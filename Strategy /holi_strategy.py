from discount_strategy import DiscountStrategy

class HolisticStrategy(DiscountStrategy):
    def get_discount(self) -> str:
        return "Holi Discount"