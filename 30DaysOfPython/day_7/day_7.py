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

 
