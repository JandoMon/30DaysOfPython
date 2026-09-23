#Q1: Ask for age and see if they can drive
print('Ask for age and see if they can drive')
age = input('Enter your age: ')
age = int(age)
if age > 18: 
    print('You are old enough to drive')
else:
    print('You need', 18 - age, 'more years to drive.')
print()

#Q2: Compare my age against someone else
print('Compare my age against someone else')
my_age = 25
person_age = input('Enter your age: ')
person_age = int(person_age)
if my_age > person_age:
    print('I am older than you by', my_age - person_age)
elif my_age < person_age: 
    print('I am younger than you', person_age - my_age)
else: 
    print('We are the same age')
print()

#Q3: Get two numbers and compare
print('Get two numbers and compare')
a = input('Enter number one: ')
b = input('Enter number two: ')
if a > b:
    print(a,'is greater than', b)
elif a < b: 
    print(a,'is less than', b)
else:
    print('The numbers are the same')
print()

#Q4: Grading system
print('Make an automatic grading system')
grade = input('Enter your grade: ')
grade = int(grade)

if grade > 89:
    print('You got an A')
elif grade > 79:
    print('You got a B')
elif grade > 69:
    print('You got a C')
elif grade > 59:
    print('You got a D')
else:
    print('You failed!')
print()

#Q5: Find the season of the year based on the month
print('Find the season of the year based on the month')
month = input('Input the month: ')

if(month == 'September' or month == 'October' or month == 'November'):
    print('It is fall')
elif(month == 'December' or month == 'January' or month == 'February'):
    print('It is winter')
elif(month == 'March' or month == 'April' or month == 'May'):
    print('It is spring')
elif(month == 'June' or month == 'July' or month == 'August'):
    print('It is summer')
print()