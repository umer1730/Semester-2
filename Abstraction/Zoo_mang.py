from abc import ABC,abstractmethod
class Entity(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Animal(Entity):
    def __init__(self,name,species,health=100):
        self.name = name
        self.species = species
        self.__health_status = health
    @property
    def manage_health(self):
        return self.__health_status
    @manage_health.setter
    def manage_health(self,value):
        if value >= 0 and value <= 100:
            self.__health_status = value
        else:
            print("Invald health value!Must be between 0 and 100")

# use dunder methods
    def __add__(self,other):
        return f"Family: {self.name} & {other.name} ({self.species})"
    def __str__(self):
        return f"Animal: {self.name} | Species: {self.species} | Health: {self.__health_status}%"
    def get_details(self):
        return self.__str__()

# multiple inheritance component        
class ElectronicTag:
    def __init__(self,tag_id):
        self.tag_id = tag_id
    def get_tag_info(self):
        return f"Tag ID: {self.tag_id}"

class TrackAnimal(Animal,ElectronicTag):
    def __init__(self,name,species,tag_id,health = 100):
        Animal.__init__(self,name,species,health)
        ElectronicTag.__init__(self,tag_id)
    def get_details(self):
        # combining methods from both parents
        return f"{Animal.get_details(self)} | {self.get_tag_info()}"    
    
def save_animal_report(animal_obj):
    try:
        filename = f"{animal_obj.name}_report.txt"  
        with open(filename,"w") as  f:
            f.write(animal_obj.get_details())
        print(f"Successfully saved report to {filename}")
    except IOError as e:
        print(f"File Error: Could not write to disk. {e}")
    except Exception as e:
        print(f"An unexcepted error occurred: {e}")

if __name__ == "__main__":
    lion = TrackAnimal("Simba","Lion","Zoo-101",95)
    print("MRO for trackanimal: ",TrackAnimal.__mro__)

    lion.health = 110
    lion.health = 85
    print(lion)

    lion2 = Animal("Nala","Lion")
    print(lion+lion2)

    save_animal_report(lion)

