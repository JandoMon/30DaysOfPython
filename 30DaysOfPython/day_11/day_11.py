from math import pi
import cmath

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

#Q3: Write a function that adds all numbers with some restrictions
print('Write a function that adds all numbers with some restrictions')
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) is not int:
            return 'This list contains an invalid argument'
        total += num
    return(total)
print('total:', add_all_nums(1, 2, 4, 5, 6))
print('total:', add_all_nums(1,2,'hello'))
print()

#Q4: Convert C to F
print('Convert C to F')
def convert_celsius_to_farenheit(celsius):
    farenheit = celsius * (9/5) + 32
    return farenheit
celsius = 21
print('Celsius to Farenheit:', celsius, 'to', round(convert_celsius_to_farenheit(celsius), 2))
print()

#Q5: Find season based on the month
print('Find season based on the month')
def check_season(month):
    if(month == 'September' or month == 'October' or month == 'November'):
        return('Fall')
    elif(month == 'December' or month == 'January' or month == 'February'):
        return('Winter')
    elif(month == 'March' or month == 'April' or month == 'May'):
        return('Spring')
    elif(month == 'June' or month == 'July' or month == 'August'):
        return('Summer')
    return None
month = 'December'
print('The month is', month,'so the season is', check_season(month))

#Q6: Calculate the slope of a linear equation
print('Write a functions that calculates the slope of a linear equation')
def calculate_slope(x_1, y_1, x_2, y_2):
    rise = y_2 - y_1
    run = x_2 - x_1
    return(rise/run)
print('Slope:', calculate_slope(1,2,2,5))
print()

#Q7: Calculate the solution set of a quadratic equation
print('Write a functions that calculates the solution set of a quadratic equation')
def calculate_quadratic_eqn(A, B, C):
    discriminat = B**2 - 4*A*C
    if(discriminat>0):
        print('Two distinct real solutions')
        solution_one = (-B + (discriminat ** .5)) / (2 * A)
        solution_two = (-B - (discriminat ** .5)) / (2 * A)
        return {solution_one, solution_two}

    elif(discriminat is 0):
        print('One repeated solution')
        solution_one = (-B + (discriminat ** .5)) / (2 * A)
        return solution_one
    else:
        print('Two imaginary solutions')
        solution_one = (-B + cmath.sqrt(discriminat)) / (2 * A)
        solution_two = (-B - cmath.sqrt(discriminat)) / (2 * A)
        return {solution_one, solution_two}
A = 1
B = 2
C = 5
print(A,'x^2 +', B, 'x +', C, '= 0' )
print('Solution of Quadratic Equation:', calculate_quadratic_eqn(A,B,C))
print()

#Q8: Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print('Write a function that takes a list as a parameter and it prints out each element of the list')
def print_lits(list):
    for item in list:
        print(item)
    print('List has been printed')
print_lits([1,5,7,2,7,8])
print()

#Q9: Write a functions that reverses a list using a loop
print('Write a functions that reverses a list using a loop')
def reverse_list(list_input):
    reversed_list = []
    for i in range(len(list_input)-1, -1,-1):
        reversed_list.append(list_input[i])
    print('List has been reversed')
    return reversed_list
new_list = reverse_list([1,2,3,4,5])
print(new_list)
print()

#Q10: Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
print('Write a function that capitalizes everything in a list')
def capitalize_list_items(list_input):
    upper = []
    for word in list_input:
        upper.append(word.upper())
    print('List has been capitalized')
    return upper
new_list = capitalize_list_items(['banana', 'apple', 'coconut', 'orange' ])
print(new_list)
print()

#Q11: Write a function that adds an item
print('Write a function that adds an item')
def add_item(list_input, item):
    return list_input + [item]
print(add_item(['apple', 'banana', 'pineapple'], 'coconut'))
    