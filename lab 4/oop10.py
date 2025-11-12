class Inventory:
    def __init__(self):
        self.products = []
    def add_products(self,name,price,quantity):
        self.products.append({"name": name,"price": price,"quantity": quantity})
        print(f"Product {name} added!")
    def show_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            print("Available products: ")
            for p in self.products:
                print(f"{p['name']}-Rs.{p['price']} (Qty: {p['quantity']})")
    def buy_products(self,name,qty):
        for p in self.products:
            if p["name"].lower() == name.lower():
                if p['quantity'] >= qty:
                    p['quantity'] -= qty
                    print(f"Purchased {qty} {p['name']}(s).")
                else:
                    print("Not enough quantity.")
                return
        print("Product not found")
inv = Inventory()
while True:
    print("1.Add product \n2.Show products \n3.Buy product \n4.Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        n = input("Enter Product name: ")
        p = float(input("Enter price: "))
        q = int(input("Enter quantity: "))
        inv.add_products(n,p,q)
    elif ch == "2":
        inv.show_products()
    elif ch =="3":
        n = input("Enter product to buy: ")
        q = int(input("Enter quantity: "))
        inv.buy_products(n,q)
    elif ch == "4":
        print("Exiting Inventory....")
        break
    else:
        print("Invalid choice")


print()
print("------")