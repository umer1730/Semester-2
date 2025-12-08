class Communication:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def phone(self,number):
        print(f"{number} confirms a call")
class Camera:
    def __init__(self,resolution_mp):
        self.resolution_mp = resolution_mp
    def take_photo(self):
        print(f"{self.resolution_mp} resolution confirms a photo capture")
class Fitness_track:
    def __init__(self,sensor_count):
        self.sensor_count = sensor_count
    def monitor_hr(self):
        print(f"{self.sensor_count} sensors confirms heart rate monitoring")
class SmartPhone(Communication,Camera):
    def __init__(self,brand,model,resolution_mp,storage_GB):
        Communication.__init__(self,brand,model)
        Camera.__init__(self,resolution_mp)
        self.storage_GB = storage_GB
        print(f"Brand: {self.brand} \nModel: {self.model} \nResolution: {self.resolution_mp} \nStorage: {self.storage_GB}")
    def stream_video(self):
        print("Confirms video streaming")
class SmartWatch(Communication,Fitness_track):
    def __init__(self,brand,model,sensor_count,battery_life):
        Communication.__init__(self,brand,model)
        Fitness_track.__init__(self,sensor_count)
        self.battery_life = battery_life
        print(f"Brand: {self.brand} \nModel: {self.model} \nSensor_count: {self.sensor_count} \nBattery life: {self.battery_life}")
    def syn_data(self):
        print(f"Confirms data synchronization")

print("\n===/ Smart phone /===")
p = SmartPhone("Apple","Iphone 15","2556+1179 pixels","512 GB / 1 TB")
p.storage_GB
p.stream_video()

print("\n===/ Samrt watch /===")
w = SmartWatch("Apple","020","e74"," 12 hours")
w.battery_life
w.syn_data()

print("\n===/ Communication /===")
c = Communication("Samsung","S22")
c.brand
c.model
c.phone("0300-1234567")

print("\n===/ Camera /===")
cam = Camera(4567)
cam.take_photo()

print("\n===/ Fitness track /===")
ft = Fitness_track(5)
ft.monitor_hr()