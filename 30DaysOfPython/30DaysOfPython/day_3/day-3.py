import math

age = 25;
person_height = 6.0; 
complex_num = 1+2j

#area of a triangle
base = int(input("Enter Base: "))
height = int(input("Enter Height: "))
area = base * height * .5
print("The area of the triangle is", area)
print()

#perimeter of a triangle
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)
print()

#area and perimeter of a rectangle 
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2*length + 2*width
print("The area of the rectangle is", area, "the perimeter is", perimeter)
print()

#area and circumference of a circle
radius = float(input("Enter radius: "))
area = radius * radius * math.pi
circumference = radius * 2 * math.pi
print("The area of the circle is", area, "and the circumference is", circumference)

#find the slope, x-intercept, y-intercept 
slope_one = 2 
y_intercept = 2
x_intercept = 1
print("For the equation y=2x-2, the slope is", slope_one,", the y-intercept is", y_intercept, "and the x-intercept is", x_intercept)
print()

#Find the slope and Euclidean distance
slope_two = (10-2)/(6-2)
eucldiean_dist = (((6-2)**2)+ ((10-2)**2))**(1/2)
print("The slope is", slope_two, "and the euclidean distance is", eucldiean_dist)
print()

#Difference between the two slopes
slope_diff = abs(slope_one - slope_two)
print("The difference in the slope is", slope_diff)
print()

#Comparing two strings 
python_len = len("python")
dragon_len = len("dragon")
print("The length of python is:", python_len)
print("The lenght of dragon is:", dragon_len)
print("python is longer" if python_len > dragon_len else "dragon is longer" if dragon_len > python_len else  "They are equal")
print()

#Use AND operator with in function
print("on is included in both words" if "on" in "python" and "on" in "dragon" else "on is not included in both words")
print()

#convert python_len to float and string
print(python_len)
print(float(python_len))
print(str(python_len))
print()

#Question 17: By using modulus,do mod 2, if the remainder is 0 then it is even, if not, then it is odd

#floor 7//2 compared to int(2.7)
print("they are equal" if 7//2==int(2.7) else "they are not equal")
print()

# "10" == 10
print("10 is not the same as '10'" if type("10") != type(10) else "10 is the same as '10'")
print()

#int(9.8) == 10
print("int(9.8) is not the same as 10" if int(9.8) != 10 else "int(9.8) is the same as 10")
print()

#Find the pay of an employee
hours = int(input("Enter your hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate 
print("You weekly earning is", pay)
print()

#Immortal
years_of_suffering = int(input("Enter the number of years you have lived:"))
print("You have lived for", years_of_suffering * 31,536,000, "seconds")
print()

#create the thingy
for i in range(1,6):
    print(i , end=" ")
    for j in range(4):
        print(i**j, end=" ")
    print()
