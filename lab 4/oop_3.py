class Bank:
    def __init__(self,deposit,withdraw):
        self.deposit = deposit
        self.withdraw = withdraw
    def display(self):
        print(f"Balance: {self.deposit - self.withdraw}")
acc = Bank(500,200)
acc.display()       