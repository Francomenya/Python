 # Python data types
# int -- it is a whole number
age = 35
print(age)
print(type(age))

# float -- it is a number with a decimal
temperature = 28.36
print(temperature)
print(type(temperature))

# boolean -- it is a value that evaluates to either true or false
raining = False
sunny = True
print(raining)
print(type(raining))

# string data type -- it is a series of characters. it can be a combination of letters, numbers, symbols or all of them that are inside of quotes
name = "Bernard"
print(name)
print(type(name))

# list -- This is a collection of items that are related in nature. It is introduced by the use of the square brackets []. A list is mutable meaning it is changeable
counties = ["Nairobi", "Nyeri", "Kisumu", "Kisii", "Mombasa", "Nakuru", "Bomet"]
print(counties)
print(type(counties))

counties.append("Lamu")
print(counties)

# tuple -- This is an unchangeable type of a list i.e the contents of the tuple do not change. It is introduced by the use of the parenthesis
names = ("John", "Kim", "Otieno", "Maral", "Kimkwet", "Janet", "Atieno")
print(names)
print(type(names))

# set - it is introduced by the use of the curly braces
numbers = {4, 85, 35, 74, 39, 75}
print(numbers)
print(type(numbers))

# Dictionary -- It orgnises data in terms of key and value pairs. It is also introduced by the use of the curly braces
phonebook = {
    "James" : 254751431312,
    "Mary" : 2547411220,
    "Jane" : 25476521635
}
print(phonebook)
print(type(phonebook))
print(phonebook["James"])