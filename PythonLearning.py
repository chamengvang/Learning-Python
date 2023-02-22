#  print is similar to console.log("")
print ("Hello World!!!")
print ('Chameng Vang')
print ('o----')
print (' |||')
print ('*' * 10)

# Variables 
age = 100 #Integer
print ("Age:" ,age)
name = "Chameng" #String
print ("Name:" ,name)
is_a_person = False #Bolean
print ("Is a Person:" ,is_a_person)

# input your answer in the terminal
# name = input("What is your name? ") 
# print("Hi " + name)
# color = input("What is your favorite color? ")
# print(name + ' likes ' + color)

# Type Conversion 

# Input will always be a string. For numbers, always add int().
# birth_year = input ('Birth Year: ')
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)
# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# Strings
course = "Python's Course for Beginners"
print(course)
course = 'Python Course for "Beginners"'
print(course)

course = '''
Hi Yall,

Here is an example of multi-line strings

ByeBye,
Okay

'''
print(course)

name = "Chameng"
print(name[0])
print(name[-1])
print(name[0:3])
print(name[1:-1])

# String Methods
course = "Python's Course for Beginners"
print(len(course)) 
# len() count the total character in a string
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.find('O'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Abosolute Beginners'))
print('Python' in course)
print('python' in course)

# Arithmetic Operations
print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 / 10)
print(10 % 10)
print(10 ** 2)
x = 10
x -= 5
print(x)

# Operator Precedence 
x = 10 + 3 * 2
print(x)
x = (2 + 3) * 10 - 3
print(x)

# Math Function 
x = 2.9
print(round(x))
print(abs(-2.9)) #abs() will always return a positive number

import math 
print(math.ceil(2.9))
print(math.floor(2.9))
# https://docs.python.org/3/library/math.html (resource)

# If Statement
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day!")
    print("Drink Plenty of Water.")
elif is_cold: #(else if)
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("WHAT A DAY!")
print("Enjoy your day!")

# Logical Operator 
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_good_credit and has_high_income:
    print("Eligible for loan")

if has_good_credit or has_high_income:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record: #and not changes the condition to true or false
    print("Eligible for loan")

# Comparison Operator > , < , <= , => , ==
temperature = 35
if temperature > 30:
    print("it's a hot day")
else:
    print("it's a cold day")

# While Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

#Guessing Game Example:
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won!!!')
#         break #this will help stop the loop
# else:
#     print('You A LOSER!!!')

# for Loop
for character in 'Python':
    print(character)

for number in range(10):
    print(number)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"total: {total} ")

# Nested Loops
for x in range(3):
    for y in range(2):
        print(f'{x},{y}')

numbers = [5,2,5,2,2]
for number in numbers:
    output = ''
    for number in range(number):
        output += 'x'
    print(output)

# Lists
names = ['Josh', 'Bob', 'Mosh']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names[-2])
print(names[-3])

numbers = [2,4,6,8,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

numbers.append(20)
print(numbers)
numbers.insert(0,30)
print(numbers)
numbers.remove(30)
# print(numbers)
# numbers.clear()
print(numbers)
numbers.pop()
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)

# Tuples - A lists but cannot be modify or change, it uses ()
numbers = (1,2,3)
numbers.count
numbers.index

# Unpacking
coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z = coordinates # the same as the code above but shorter
print(f'{x},{y},{z}')

# Dictionaries (objects)
customer = {
    "name": "John Smith",
    "age": 100,
    "is_verified": True
}
print(customer)
print(customer["name"])
print(customer.get("NAME"))

# phone = input("phone: ")
# digits = {
#     "1": 'One',
#     "2": 'Two',
#     "3": 'Three',
#     "4": 'Four'
# }
# output = ""
# for character in phone:
#     output += digits.get(character, "!") + " "
# print(output)