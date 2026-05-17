import dataclasses

from CabBooking.cab_type import CabType

@dataclasses
class Cab:
    cab_id: int
    cab_type: CabType
    licese_plate: str
