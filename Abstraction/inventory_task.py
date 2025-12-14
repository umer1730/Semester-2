class Product:
    Tax_Rate = 0.05
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def display_price_with_tax(self):
        final_price = self.price + (self.price * Product.Tax_Rate)
        return f"Final price of {self.name}: {final_price}"
    
    @classmethod
    def set_tax_rate(cls,new_rate):
        cls.Tax_Rate = new_rate

    @staticmethod
    def is_valid(price):
        return price > 0 
    
p1 = Product("Mouse",1200)
p2 = Product("Handfree",1000)
print(p1.display_price_with_tax())
print(p2.display_price_with_tax())

Product.set_tax_rate(0.10)
print(p1.display_price_with_tax())
print(p2.display_price_with_tax())