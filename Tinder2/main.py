from Tinder2.enums import Gender, SwipeAction
from Tinder2.location import Location
from Tinder2.tinder import Tinder2
from Tinder2.user import User
from Tinder2.user_preference import Interest


def run_demo() -> None:
    app = Tinder2()

    alice = User("Alice", 26, Gender.FEMALE, Location(12.9716, 77.5946))
    alice.get_user_preferences().min_age = 24
    alice.get_user_preferences().max_age = 32
    alice.get_user_preferences().genders = [Gender.MALE]
    alice.get_user_preferences().distance_km = 10
    alice.get_user_profile().add_interest(Interest("music", "hobby"))
    alice.get_user_profile().add_interest(Interest("coffee", "lifestyle"))

    bob = User("Bob", 28, Gender.MALE, Location(12.975, 77.60))
    bob.get_user_preferences().min_age = 22
    bob.get_user_preferences().max_age = 30
    bob.get_user_preferences().genders = [Gender.FEMALE]
    bob.get_user_preferences().distance_km = 10
    bob.get_user_profile().add_interest(Interest("music", "hobby"))

    charlie = User("Charlie", 40, Gender.MALE, Location(15.0, 80.0))
    charlie.get_user_preferences().genders = [Gender.FEMALE]

    app.register_user(alice)
    app.register_user(bob)
    app.register_user(charlie)

    pending = app.swipe(alice.get_id(), bob.get_id(), SwipeAction.RIGHT)
    print("Here: ", pending)

    match = app.swipe(bob.get_id(), alice.get_id(), SwipeAction.RIGHT)
    print(match)
    if match:
        conversation = app.get_conversation(match.id)
        print(conversation)
        m1 = app.send_message(match.id, alice.get_id(), "Hey Bob, nice to match with you!")
        m2 = app.send_message(match.id, bob.get_id(), "Hi Alice, same here.")
        print(m1)
        print(m2)
        print(app.list_messages(match.id))
        app.mark_messages_read(match.id, alice.get_id())
        print(app.list_messages(match.id))

    no_match = app.swipe(alice.get_id(), charlie.get_id(), SwipeAction.RIGHT)
    print(no_match)

    match2 = app.swipe(bob.get_id(), alice.get_id(), SwipeAction.RIGHT)
    print(match2)

    print("All matches:")
    for item in app.list_matches():
        print(item)


if __name__ == "__main__":
    run_demo()
