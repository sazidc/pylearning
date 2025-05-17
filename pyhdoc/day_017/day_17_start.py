# Day-17 working with class

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "mikaela")
user_2 = User("002", "johnny")

print(user_1.id)
print(user_1.username)

print(user_2.id)
print(user_2.username)
