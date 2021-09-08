class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0


user1 = User(1, "suriya")
user2 = User(2, "ganesh")
print(user1.followers)