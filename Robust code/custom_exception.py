class PaymentError(Exception):
    pass
class InsufficientFundsError(PaymentError):
    pass
class InvalidAmountError(PaymentError):
    pass
class PaymentGatewayError(PaymentError):
    pass
def process_order(amount,user_balance):
    if amount > user_balance:
        raise InsufficientFundsError(f"Need ${amount - user_balance} more")
    if amount <= 0:
        raise InvalidAmountError(f"${amount} is invalid")
process_order(100,90)

print()
class AgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise AgeError("Age ust be 18 or above")
    return "Access granted"
try:
    print(check_age(15))
except AgeError as e:
    print(e)