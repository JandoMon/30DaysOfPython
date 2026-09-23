# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Q1: Find the length of the of the set it_companies
print('Find the length of the of the set it_companies')
print(len(it_companies))
print()

#Q2: Add Twitter to companies
print('Add Twitter to companies')
it_companies.add('Twitter')
print(it_companies)
print()

#Q3: Insert mulitple it_companies at once to the set
print('Insert mulitple it_companies at once to the set')
it_companies.update(['Texas Instrument', 'ASUS', 'MSI'])
print(it_companies)
print()

#Q4: Remove one of the companies from the set
print('Remove one of the companies from the set')
it_companies.remove('MSI')
print(it_companies)
print()

#Q5: What is the difference between move and discard
print('What is the difference between move and discard')
print('The main difference between move and discard is how they handle items that are not present in the set.' \
'remove function will raise an error if no item exist in the set, while discard will not.', end = '\n\n')

#Q6: Join A and B
print('Join A and B')
C = A.union(B)
print(C)
print()

#Q7: Intersection of A and B
print('Intersection of A and B')
print(A.intersection(B))

#Q8: Are A and B disjoint sets
print('Are A and B disjoint sets')
print(A.isdisjoint(B))
print()

#Q9: Join A with B and B with A 
print('Join A with B and B with A')
join_AB = A.union(B)
join_BA = B.union(A)
print(join_AB,'&&', join_BA)
print()

#Q10: Symmetric difference of A && B
print('Symmetric difference of A && B')
sym_diff = A.symmetric_difference(B)
print(sym_diff)
print()

#Q11: Delete the set entirely 
del A
del B
try:
    print(A)
except NameError:
    print("Success: The Set 'A' no longer exists.")

try:
    print(B)
except NameError: 
    print("Success: The Set 'B' no longer exists.")
print()

 
#Q12: Convert the ages to a set and compare the length of the list vs set
print('Convert the ages to a set and compare the length of the list vs set')
ages_st = set(age)
print(('They are the same' if len(ages_st)== len(age) else 'They are the different lenghts'))
print()

#Q13: Explain the difference between the following data types: string, list, tuple and set
print('Explain the difference between the following data types: string, list, tuple and set')
print('A String is a just a string of letters or words that is immutable and ordered. \n' \
'A list is a collection of objects that are ordered and can have duplicates.\n' \
'A tuple is a collection of objects that are ordered but cannot be changed once createdn\n' \
'A Set is a collection of objects that are unordered and do not allow duplicates')
print()

#Q14: I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
print('I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.')
sentence = 'I am a teacher and I love to inspire and teach people.'
lst = sentence.split()
st = set(lst)
print(len(st))