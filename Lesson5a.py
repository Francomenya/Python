# Functions in python:
# A function is a block of statement that performs an action. 
# We have two main types of functions i.e 1. in built functions 2. user defined functions
# The in built functions come pre-installed with the python interpreter examples include print(), type(), append() etc.
# 2. User defined functions: They are the function that have been built by the user specifically to solve a task that suites the program the developer is coming up. To create user defined function we use the def keyword which means define. Followed by the name of the function and the body of the function.

# when you define a function, for it to give you some output you need to invoke the function i.e call it. You do so outside the body of the function.

# example 1 below:
def greeting():
    print("Hello there.")


greeting()
print("==========================")

# Below is a function that is able to add two numbers
def summation():
    number1 = 15
    number2 = 20
    sum = number1 + number2
    print("The sum of the two numbers is: ", sum)


summation()

print("=============================")
# Below is a third example
# Create a function that is able to calculate the area of rectangle given the length as 30 and width as 15
def areaOfRectangle():
    length = 40
    width = 15
    area = length * width
    print("The area of the rectangle is: ", area)


areaOfRectangle()

print("=============================")
# create a function that calculates the simple interest gained after a person invested 70000 in a bank that pays an interest rate of 7% for a period of 8 years.
# simpleInterest = (p * r * t)/100
def simpleinterest():
    principle = 70000
    rate = 7
    time = 8
    interest = (principle * rate * time)/100
    print("The simple intrests is: ", interest)

simpleinterest()
