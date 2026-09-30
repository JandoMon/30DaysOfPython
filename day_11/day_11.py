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