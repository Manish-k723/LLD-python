class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def is_adult(self) -> bool:
        return self.age >= 18

    def save_to_db(self):
        print("connect to database")
        print(f"Saving user to database {self.name}")
        print("Disconnecting from database")

    def remove_from_db(self):
        print("connect to database")
        print(f"Removing user from database{self.name}")
        print("Disconnecting from database")

    def send_email(self):
        print(f"Sending email to {self.name}")

user = User("John", 20)
user.save_to_db()
