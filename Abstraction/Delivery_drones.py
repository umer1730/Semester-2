from abc import ABC,abstractmethod
class SafetyError(Exception):
    pass
class Robot(ABC):
    @abstractmethod
    def perform_task(self):
        pass
class FlyingVehicle(Robot):
    def __init__(self,altitude,**kwargs):
        super().__init__(**kwargs)
        self.altitude = altitude
        print("Flying capabilities initialized")
class PackageHandler(Robot):
    def __init__(self,loadweight,**kwargs):
        super().__init__(**kwargs)
        self.loadweight = loadweight
        print("Package handling intialized")
class DeliveryBrone(FlyingVehicle,PackageHandler):
    def __init__(self,name,battery_level,loadweight,altitude):
        super().__init__(altitude,loadweight)
        self.name = name
        self._battery_level = battery_level
    
    @property
    def battery_level(self):
        return self._battery_level
    
    @battery_level.setter
    def battery_level(self,value):
        if not (0 <= value <= 100):
            raise ValueError("Battery must e between 0 and 100")

        if self.value < 10 and self.loadweight > 20:
            raise SafetyError("Danger: Low battery with heavy load")
        self._battery_level = value
    
    def perform_task(self):
        return f"Drone {self.name} is delivering a {self.loadweight}Kg package at {self.altitude}m"
try:
    
    my_drone = DeliveryDrone(name="SkyLifter-X", battery_level=50, load_weight=25, altitude=100)
    print(my_drone.perform_task())
    
    print("Updating battery to 5%..")
    my_drone.battery_level = 5  
    print(f"Caught a Safety Issue: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    