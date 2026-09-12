#Q1: Create an empty tuple
print('Create an empty tuple')
tpl = tuple()
print(tpl)
print()

#Q2: Create a tuple of imaginary siblings
print('Create a tuple of imaginary siblings')
brothers = ('Chris', 'Mikey', 'Matthew')
sisters = ('Noella', 'Naomi', 'Lily')
print(brothers)
print(sisters)
print()

#Q3: Join the lists of brothers and sisters
print('Join the lists of brothers and sisters')
siblings = brothers + sisters
print(siblings)
print()

#Q4: How many siblings 
print('How many siblings')
print(len(siblings))
print()

#Q5: Add something to the tuple
print('Add a father and mother ')
siblings = list(siblings)
parents = ['Juan', 'Olga']
siblings.extend(parents)
family_members = tuple(siblings)
print(family_members)
print()

#Q1: Unpack siblings, mother and father
print('Unpack siblings, mother and father')
*siblings, mother, father = family_members
print(siblings)
print(mother)
print(father)
print()

#Q2: Create a tuple for fruits, vegetable, and animal products
print('Create a tuple for fruits, vegetables, and animal products')
fruits = 'banana', 'apple', 'mango', 'strawberry'
vegetables = 'onion', 'lettuce', 'tomato', 'cucumber'
animal_products = 'milk', 'honey', 'cheese', 'beef'
print(fruits)
print(vegetables)
print(animal_products)
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
print()

#Q3: Change the tuple to a list
print('Change the tuple to a list')
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print()

#Q4: Slice the middle of the list
print('Slice out the middle of the list')
middle_item_index = int((len(food_stuff_lt)-1)/2)
middle_item = food_stuff_lt[middle_item_index]
print(middle_item)
print()

#Q5: Slice first three and last three
print('Slice out the first three and last three')
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-4:-1]
print(first_three)
print(last_three)
print()

#Q6: Delete food tuple
print('Delete food tuple')
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print("Success: The variable 'x' no longer exists.")
print()

#Q7: Check values in tuple
print('Check values in tuple')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
print()
