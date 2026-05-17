from User import User

class UserRepo:
    def __init__(self, db):
        self.db = db
        self.client = None # Redis(db_path)

    def get_client(self):
        if self.client is None:
            self.client = self.db.get_client()
        return self.client

    def save_user(self, user: User):
        print(f"Saving user to database {user.name}")
        # self.get_client().set(user.name, user)

    def remove_user(self, user: User):
        print(f"Removing user from database {user.name}")