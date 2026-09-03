import math
#Day 2: 30 Days of python programming

#Excercise 1
first_name = "Paul"
last_name = "Montano"
full_name = first_name + " " + last_name
country = "USA"
city = "Cypress"
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = False
is_Hungry, fav_fast_food, is_Tired = True, "McDonald", True

#Excercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_Hungry))
print(type(fav_fast_food))
print(type(is_Tired))

print(len(first_name))
#ternary operator
print("My first name is longer!" if len(first_name) > len(last_name) else "My last name is longer!")
num_one = 5
num_two = 4
print(num_one)
print(num_two)
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one * num_two
print(division)
modulus = num_two % num_one
print(modulus)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

radius = input("Input radius:")
#area of a circle pi*r^2 
area_of_circle = math.pi * (float(radius) ** 2)
print(area_of_circle)

#circumference of a circle 2pi*r
circumference_of_circle = 2 * math.pi * float(radius)
print(circumference_of_circle)

first_name = input("Input First Name: ")
last_name = input("Input Last Name: ")
country = input("Input Country: ")
age = input("Input Age: ")

print("Here is you Personal Information: ")
print(first_name)
print(last_name)
print(country)
print(age)

help('keywords')




