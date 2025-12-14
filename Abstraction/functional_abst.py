#Functional abstraction means hiding the internal working of a function and showing only what the function does, not how it does it
class Order:
    def __init__(self,items):
        self.items = items
    def process_order(self):
        if self._validate_stock():
            self._charge_customer()
            self._log_transaction()
            print("Order processed successfully")
            return True
        return False
    def _validate_stock(self):
        return True
    def _charge_customer(self):
        pass
    def _log_transaction(self):
        pass
order = Order(["Shoes", "Bag"])
order.process_order()
