from User import User
from UserRepo import UserRepo
from emailSender import EmailSender

email_sender = EmailSender(UserRepo(None))
user = User("John", 20, )
db = UserRepo("sqlite:////tmp/users.db")
db.save_user(user)
