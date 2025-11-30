# class PasswordManager:
#     def __init__(self,password):
#         self.__password = password
#     def set_pass(self,old_pass,new_pass):
#         if old_pass == self.__password:
#             self.__password = new_pass
#             print("Password Updated")
#         else:
#             print("access denied")
# pas = PasswordManager(1234)
# print(pas.get_pass)
# pas.get_pass = 5678
# print(pas.get_pass)
class PasswordManager:
    def __init__(self,password):
        self.__password = password
    def set_pass(self,old_pass,new_pass):
        if old_pass == self.__password:
            self.__password = new_pass
            print("Password Updated")
        else:
            print("Access denied")
p = PasswordManager(1234)
p.set_pass(1234,5678)
p.set_pass(9999,2762)