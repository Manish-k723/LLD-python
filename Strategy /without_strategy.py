class Discount:
    def get_discount(self, code: str) -> str:
        if code == "10OFF":
            return "10% off"
        if code == "20OFF":
            return "20% off"
        return "Invalid code"

discount = Discount()
print(discount.get_discount("10OFF"))