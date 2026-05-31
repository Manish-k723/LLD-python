from Tinder.enums import Gender, SwipeAction
from Tinder.location import Location
from Tinder.tinder import Tinder
from Tinder.user import User
from Tinder.user_preference import Interest


def start_tinder():
    tinder = Tinder()

    manish = User("Manish", 25, Gender.MALE, Location(12.9716, 77.5946))
    manish.get_user_preferences().set_min_age(20)
    manish.get_user_preferences().set_max_age(32)
    manish.get_user_preferences().set_distance(10)
    manish.get_user_preferences().add_gender(Gender.FEMALE)
    manish.get_user_profile().add_interest([Interest("music", "hobby"), Interest("coffee", "lifestyle")])

    penka = User("Penka", 22, Gender.FEMALE, Location(12.975, 77.60))
    penka.get_user_preferences().set_min_age(20)
    penka.get_user_preferences().set_max_age(28)
    penka.get_user_preferences().set_distance(15)
    penka.get_user_preferences().add_gender(Gender.MALE)
    penka.get_user_profile().add_interest([Interest("movies", "hobby"), Interest("music", "lifestyle")])
    tinder.register_user(manish)
    tinder.register_user(penka)

    match = tinder.swipe(penka.get_id(), manish.get_id(), SwipeAction.RIGHT)
    print(match)

    match2 = tinder.swipe(manish.get_id(), penka.get_id(), SwipeAction.RIGHT)
    print(match2)

    for match in tinder.get_matches():
        print(match)

if __name__ == "__main__":
    start_tinder()