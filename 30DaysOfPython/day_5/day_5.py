#Q1: Declare an empty list
print('Q1: Declare an empty list')
empty_lst = []
print(empty_lst)
print()

#Q2: Declare a list with 5 items
print('Q2: List with 5 items')
five_item_lst = [1,2,3,4,5]
print(five_item_lst)
print()

#Q3: Find the length of the list
print('Q3: Length of List')
print(len(five_item_lst))
print()

#Q4: Get the first item, middle item, last item
print('Q4: First item, Middle item, Last item')
print(five_item_lst[0], five_item_lst[int((len(five_item_lst)-1)/2)], five_item_lst[len(five_item_lst)-1])
print()

#Q5: Declare a list of mixed data types
print('Q5: Declare a list of mixed data types')
print(['Paul', 25, '6ft', 'single', '12603 wouldnt you like to know'])
print()

#Q6: Declare list
print('Q6: Declare a list of IT companies')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print()

#Q7: print the list
print('Q7: Print the list')
print(it_companies)
print()

#Q8: number of companies in the list
print('Q8: Num of companies in the list')
print(len(it_companies))

#Q9: First, Middle, Last Company
print('Q9: First, Middle, Last Company')
print(it_companies[0], it_companies[int((len(it_companies)-1)/2)], it_companies[len(it_companies)-1])
print()

#Q10: Print the list after modifying the list
print('Q10: Print the list after modifying the list')
it_companies[0]= 'X'
print(it_companies)
print()

#Q11: Add an IT company to the list
print('Q11: Add an IT Compnay to the list')
it_companies.append('TI')
print(it_companies)
print()

#Q12: Insert an IT company in the middle of the companies list
print('Q12: Insert an IT company in the middle of the companies list')
middle_IT= int((len(it_companies)-1)/2)
it_companies.insert(middle_IT, 'NIVIDIA')
print(it_companies)
print()

#Q13: Change one of the IT companies to uppercase
print('Q13: Change one of the IT companies to uppercase')
index_apple = it_companies.index('Apple')
it_companies[index_apple] = it_companies[index_apple].upper()
print(it_companies)
print()

#Q14: Join the IT companies with '#; ' 
print('Join the IT companies with #;')
print('#; '.join(it_companies))
print()