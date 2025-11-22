class Temperature:
    def __init__(self,c):
        self.__celcius = c
    def get_temp(self):
        return 9 / 5 * self.__celcius+32
temp = Temperature(25)
print(temp.get_temp())