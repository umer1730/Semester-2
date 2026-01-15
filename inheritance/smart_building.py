class TemperatureSensor:
    def __init__(self,temp_threshold=50):
        self.temp_threshold = temp_threshold

class MonitorSensor:
    def __init__(self,sensitivity="high"):
        self.sensitivity  = sensitivity

class SmartSecuritySystem(TemperatureSensor,MonitorSensor):
    def __init__(self,temp_threshold,sensitivity,model_name):
        super().__init__(temp_threshold=temp_threshold,sensitivity = sensitivity)
        self.model_name = model_name

    def check_threat(self,current_temp,motion_detected):
        if current_temp > self.temp_threshold and motion_detected:
            return f"Alert: {self.model_name} detected a fire or break-in"
        return "System Secure"
    
print(SmartSecuritySystem.__mro__)        