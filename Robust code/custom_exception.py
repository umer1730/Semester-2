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