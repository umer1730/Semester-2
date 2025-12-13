class User:
    def __init__(self,username,login_count=0):
        self.username = username
        self.login_count = login_count
    def login(self):
        self.login_count += 1
        print(f"{self.username} logged in. Total logins: {self.login_count}")
    def check_status(self):
        return f"{self.username} has logged in {self.login_count} times."
user_1 = User("Alice")
user_2 = User("Bob",login_count=5)
user_1.login()
user_1.login()
print(user_1.check_status())
print(user_2.check_status())

