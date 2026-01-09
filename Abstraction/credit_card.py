from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")
class Checkout:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method
    def process_payment(self, amount):
        self.payment_method.pay(amount)
checkout = Checkout(PayPalPayment())
checkout.process_payment(500)
