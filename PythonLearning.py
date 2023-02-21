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