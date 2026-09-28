from math import pi

#Q1: Declare a function add_two_numbers. It takes two parameters and it returns a sum
print('Write a function that adds two numbers')
def add_two_numbers(num_one, num_two):
    return  num_one + num_two
num_one = 5
num_two = 3
print('Sum:',num_one, '+', num_two, "=",  add_two_numbers(5,3))
print()

#Q2: Write a function that writes area of a circle
print('Write a function that finds the area of a circle')
def area_of_circle(radius):
    return radius * radius * pi
radius = 5;
print('Area for radius of', radius, ':', area_of_circle(5))
print()
