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

#Q6: If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a fruit: ')
if not new_fruit in fruits:
    print('Not in list! Will add now!')
    fruits.append(new_fruit)
    print(fruits)
else:
    print('That fruit already exists in the list')
print()

#Q7: Do task on person
print('Do a background check! ')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if not person: 
    print('I have no skills')
else:
    middle_index = int((len(person))/2)
    print('Middle Skill: ', person['skills'][middle_index])
print()

is_Python = 'Python' in person['skills']
if not person: 
    print('I have no skills')
elif is_Python:
    print('Has Python skills')
else:
    print('Has no Python skills')
print()

#Q7: 
# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:

is_Javascript = 'Javascript' in person['skills']
is_React = 'React' in person['skills']
is_Node = 'Node' in person['skills']
is_Python = 'Python' in person['skills']
is_MongoDB = 'MongoDB' in person['skills']

print('Job Title Assignment/Assessment:')
if is_Javascript and is_React:
    print('He is a front end developer')
elif is_Node and is_Python and is_MongoDB:
    print('He is a backend developer ')
elif is_React and is_Node and is_MongoDB:
    print('He is a fullstack developer')
else: 
    print('unknown title')

is_Married = person['is_married']
is_Finland = person['country']

if is_Married and  is_Finland:
    print(person['first_name'], person['last_name'], 'lives in', person['country'], '. He is married')
else:
    print('He is not married or he does not live in Finland')