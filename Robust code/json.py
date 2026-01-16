import json
JSON_CONFIG = "config.json"
with open(JSON_CONFIG,"r") as f:
    config_data = json.load(f)

print(f"Loaded 'muted' status: {config_data['muted']}")
config_data['muted'] = False

print()
import json
from abc import ABC,abstractmethod
class StorageInterface(ABC):
    @abstractmethod
    def save(self,data):
        pass

class JsonStorage(StorageInterface):
    def __init__(self,filename):
        self.filename = filename
    
    def save(self,data):
        try:
            with open(self.filename, "w") as f:
                json.dump(data, f,indent = 4)
            print("Data save ")
        except IOError as e:
            print(f"File error: Could not write to file. {e}")
        finally:
            print("Cleanup: File operation closed")
data_to_save = {"user": "admin", "access_level": 5, "status": "active"}
storage = JSONStorage("settings.json")
storage.save(data_to_save)