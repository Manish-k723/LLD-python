from datetime import datetime

from Tinder.enums import SwipeAction


class Swipe:
    def __init__(self, user_id1: int, user_id2: int, action: SwipeAction):
        self._from_user = user_id1
        self._to_user = user_id2
        self._action: SwipeAction = action
        self._match_timestamp = datetime.now()

    
