class Temperature:
    def __init__(self,celcius):
        self.__celcius = celcius
    @property
    def get_temp(self):
        return (9/5*self.__celcius)+32
    @get_temp.setter
    def get_temp(self,temp):
        if isinstance(temp,int):
            self.__celcius = temp 
        else:
            print("temp cannot be negative")    
t = Temperature(25)
print(f"Fahrenheit: {t.get_temp}")
t.get_temp = 35
print(f"Fahrenheit: {t.get_temp}")
print(t._Temperature__celcius)  #we can access private attribute