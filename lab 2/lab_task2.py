# grade calculator
score = int(input("Enter score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(f"Grade: {grade}")

print()
#loops
i = 1
while(i<100):
    i+=1
    print("number",i)
print("loop ended")

print()
# print numbers from 100 to 1
i = 100
while(i>=1):
    print("number",i)
    i-=1
print("loop ended")

print()
list = [1,2,3,4,5]
for i in range(0,len(list),1):
    print(list[i], end=" ")
    print(list[i])

