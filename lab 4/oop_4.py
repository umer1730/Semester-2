class Phone:
    def __init__(self):
        self.contacts = []
    def add_contacts(self,name):
        if name not in self.contacts:
            self.contacts.append(name)
            print(f"{name} added to contacts")
        else:
            print(f"{name} is not added")
    def remove_contacts(self,name):
        if name in self.contacts:
            self.contacts.remove(name)
            print(f"{name} remove from contacts")
        else:
            print(f"{name} not remove from contacts")
    def show_contacts(self):
        print(f"Contacts: {self.contacts}")
p1 = Phone()
p1.add_contacts("Bob")
p1.add_contacts("Charlie")
p1.show_contacts()
p1.remove_contacts("Bob")
p1.show_contacts()
p1.remove_contacts("Alice")
p1.remove_contacts("Charlie")
p1.show_contacts()
