class Cart:
    def __init__(self,name,cart_price):
        self.name = name
        self.cart_price = cart_price
    def __it__(self,other):
        return self.cart_price < other.cart_price
    def __gt__(self,other):
        return self.cart_price > other.cart_price
    def __eq__(self,other):
        return self.cart_price == other.cart_price
    def __str__(self):
        return f"{self.name} - Total Price: {self.cart_price}"
crt1 = Cart("ali",222)
crt2 = Cart("ali",222)
print(crt1<crt2)
print(crt1>crt2)
print(crt1==crt2)