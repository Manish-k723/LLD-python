from discount_service import DiscountService
from diwali_strategy import DiwaliStrategy
from holi_strategy import HolisticStrategy

strategy = DiwaliStrategy()
discount_service = DiscountService(strategy)
print(discount_service.process_payment())

discount_service.set_strategy(HolisticStrategy())
print(discount_service.process_payment())