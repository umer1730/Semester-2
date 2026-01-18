class Tea:
    def prepare(self):
        raise NotImplementedError("This method must be overridden")

class Kashmiri_tea(Tea):
    def __init__(self,milk,salt,sugar,green_tea):
        self.__milk = milk
        self.__salt = salt
        self.__sugar = sugar
        self.__green_tea = green_tea
    def prepare(self):
        print("Boiling water")
        print(f"Adding green tea leaves: {self.__green_tea}")
        print(f"Adding milk: {self.__milk}")
        print(f"Adding salt: {self.__salt}")
        print(f"Adding sugar: {self.__sugar}")
        print("Simmering until pink color appears")
        print("Kashmiri tea is ready!")

class Almond(Kashmiri_tea):
    def prepare(self):
        super().prepare()
        print("Adding crushed almonds")
        print("Almond kashmiri tea is ready")

class Order:
    def __init__(self,tea_type):
        self.tea_type = tea_type
    def serve(self):
        print("\n---Prepairing Order---")
        self.tea_type.prepare()
        print("Serving tea to customer")
        print("-----------------")

simple_tea = Kashmiri_tea(
    milk = "2 cups",
    salt = "1 pinch",
    sugar="1 tea spoon",
    green_tea="2 tea spoon"
)
order_1 = Order(simple_tea)
order_1.serve()

almond_tea = Almond(
    milk = "2 cups",
    salt = "1 pinch",
    sugar = "1 tea spoon",
    green_tea="2 tea spoon"
)
order_2 = Order(almond_tea)
