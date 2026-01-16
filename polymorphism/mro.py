class A:
    def show(self):
        print("A show")
class B(A):
    def show(self):
        print("b show")
class C(A):
    def show(self):
        print("C show")
class D(B,C):
    def show(self):
        print("B and c show")
obj = D()
obj.show()
print(D.mro())

print()
class Logger:
    def log(self, message):
        print(f"Logger: {message}")
class Authenticator:
    def authenticate(self, user):
        print(f"Authenticating {user}")

    def log(self, message):
        print(f"Authenticator log: {message}")
class SecureLogger(Logger, Authenticator):
    def log(self, message):
        print(f"SecureLogger: {message.upper()}")

secure = SecureLogger()
secure.log("This is a test")      
secure.authenticate("Alice")      
