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
