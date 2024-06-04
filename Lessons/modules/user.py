class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.hashed_password = self.hash_password(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname} : {self.age} лет."

    def __repr__(self):
        return f"User({self.nickname}, {self.hashed_password}, {self.age})"

    @staticmethod
    def hash_password(password):
        return hash(password)

    def check_login(self, login, password):
        if self.nickname == login and self.hash_password(password) == self.hashed_password:
            return True
        else:
            return False
