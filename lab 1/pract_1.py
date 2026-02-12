text = "hello"
print("Text is: ", text[1:4])

list = [1,2,3,4,5,6,7,8]
print("Slicing list is:",list[1::2])

# traffic signals
print()
print("---traffic light---")
light = input("Enter color: ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("ready")
elif light == "green":
    print("move")
else:
    print("Invalid output")

print()
# grading systems
print("---Grading system----")
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A+")
elif marks >= 85:
    print("A")
elif marks >= 80:
    print("A-")
elif marks >= 75:
    print("B+")
elif marks >= 70:
    print("B")
elif marks >= 65:
    print("B-")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else: 
    print("F")

# weather systems
print()
print("----weather system-----")
month = input("Enter month: ")
if month in ["December", "January", "February"]:
    print("Winter season")
elif month in ["June", "July"]:
    print("Summer season")
elif month in ["August", "September"]:
    print("Rainy season")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["October", "November"]:
    print("Autumn")
else:
    print("Invalid month")

# Time table
print()
print("----time table----")
subjects = input("Enter subjects name: ")
if subjects == "Software Engineering":
    print("Monaday 2 to 3 p.m and Thursday 3 to 5 p.m ")
elif subjects == "MVC":
    print("Monday 12 to 1 p.m and Tuesday 2 to 4 p.m")
elif subjects == "Linear algebra":
    print("Monday 3 to 5 p.m and Tuesday 12 to 1 p.m")
elif subjects == "Tech writing":
    print("Tuesday 1 to 2 p.m and Wednesday 3 to 5 p.m")
elif subjects == "Applied Physics":
    print("Wednesday 1 to 3 p.m")
elif subjects == "AP lab":
    print("Tuesday 4 to 6 p.m")
elif subjects == "OOP":
    print("Thursday 12 to 3 p.m")
elif subjects == "OOP lab":
    print("Friday 8 to 11 p.m")
else:
    print("Invalid subjects")

print()
print("----discount day----")
days = input("Enter day:")
if days in ["Monday","Tuesday"]:
    print("10% discount")
elif days in ["Wednesday","Thursday"]:
    print("20% discount")
elif days in ["Friday","Saturday"]:
    print("50% discount")
elif days in ["Sunday"]:
    print("70% discount")
else:
    print("Invalid day")


print()
cars = ["Volvo","BMW","Ford","Mazda","Tesla"]
for i in cars:
    print(i)

print(cars[2])