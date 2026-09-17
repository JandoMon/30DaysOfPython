#Q1: Create an empty dictionary called dog 
print('Create an empty dictionary called dog')
dog = {}
print(dog)
print()

#Q2: Add name, color, breed, legs, age to the dog dictioanry 
print('Add name, color, breed, legs, age to the dog dictioanry')
dog['name'] = 'jando'
dog['color'] = 'brown'
dog['breed'] = 'shar pei'
dog['legs'] = '3'
dog['age'] = '6'
print(dog)
print()

#Q3: Create a student dictionary 
print('Create a student dictionary')
stu_dict = {}
stu_dict['first_name'] = 'Jando'
stu_dict['last_name'] = 'Montano'
stu_dict['gender'] = 'M'
stu_dict['age'] = '25'
stu_dict['martial_status'] ='single and sad'
stu_dict['skills'] = ['sorta tall', 'sorta funny', 'sorta ugly']
stu_dict['country'] = 'USA'
stu_dict['city'] = 'Houston'
stu_dict['address'] = 'Wouldnt you like to know, weather boy'
print(stu_dict)
print()

#Q4: Get the length of student dictionary
print('Get the length of student dictionary')
print(len(stu_dict))
print()

#Q5: Get the value of skills and check data type
print('Get the value of skills and check data type')
skills = stu_dict.get('skills')
print(type(skills))
print()

#Q6: Modify the skills values by adding one or two skills 
print('Modify the skills values by adding one or two skills')
stu_dict.get('skills').append('sorta code')
print(stu_dict['skills'])
print()

#Q7: Get the dictionary keys as a list
print('Get the dictionary keys as a list')
print(stu_dict.keys())
print()

#Q8: Get the dictionary values as a list
print('Get the dictionary values as a list')
print(stu_dict.values())
print()

#Q9: Change the dictionary to a list of tuples using items() method
print('Change the dictionary to a list of tuples using items() method')
print(stu_dict.items())
print()

#Q10: Delete one of the items in the dictionary
print('Delete one of the items in the dictionary')
del stu_dict['skills']
print(stu_dict)
print()

#Q11: Delete one of the dictionaries
print('Delete one of the dictionaries')
del stu_dict
try:
    print(stu_dict)
except NameError: 
    print("Success: The Set 'stu_dict' no longer exists.")
print()