from Tinder.enums import MatchType
from Tinder.matcher import AgeMatcher


class MatcherFactory:
    @staticmethod
    def create_matcher(match_type: MatchType):
        if match_type == MatchType.AGE:
            return AgeMatcher()
        elif match_type == MatchType.LOCATION:
            return LocationMatcher()
        else:
            return None