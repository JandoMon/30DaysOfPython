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