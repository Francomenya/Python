# Function with parameters.
# Parameters are values that act as argument when invoking a function. Functions with parameters allows us to reuse different types of functions

def greeting(name):
    print("Hello: ", name,"How have you been?")


greeting("James")
greeting("Pauline")
greeting("Mary")

print("======================")
def communication(names):
    print("Hello member: ",names,"Hope this finds you well, We would like to inform you of our upcoming general meeting to be held....")


communication("James Otino")
communication("Mary Sigon")
communication("Fatuma Gendi")

print("======================")
# Below is a function that is able to add multiple numbers
def addition(number1, number2, number3):
    sum = number1 + number2 + number3
    print("The sum of the numbers is: ", sum)

addition(45, 60, 78)
addition(78, 32, 65)
addition(10, 5, 25)

print("======================")
# create a function that find the area of three triangles. 1) 40, 12 2) 60, 40 3) 70, 15.
# area of triangle = 0.5 * base * height
def areaoftriangle(base, height):
    areaoftriangle = 0.5 * base * height
    print("The area of triangle is: ", areaoftriangle)

areaoftriangle(40,12)
areaoftriangle(60,40)
areaoftriangle(70,15)
