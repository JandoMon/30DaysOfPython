#Q1: Concatenating 
thirty = 'Thirty'
days = 'Days'
of = 'Of'
python ="Python"
space = ' '
python_30 = thirty + space + days + space + of + space + python
print(python_30)
print()

#Q2: Concatenating
coding = 'Coding'
for_ = 'For'
all_ = 'All'
space = ' '
coding_for_all = coding + space + for_ + space + all_
print(coding_for_all)
print()

#Q3: string variable
company = "Coding for All"

#Q4: print variable
print(company)
print()

#Q5: print len
print(len(company))
print()

#Q6: uppercase
print(company.upper())
print()

#Q7: lowercase
print(company.lower())
print()

#Q8: capitalize, title, swapcase
coding_for_all = "Coding For All"
print(coding_for_all.capitalize())
print(coding_for_all.title())
print(coding_for_all.swapcase())
print()

#Q9: slice the for word in Coding For All
print(coding_for_all[0:6])
print()

#Q10: Check to see if Coding is in the word
print(coding_for_all.index('Coding'))
print(coding_for_all.find('Coding'))
print()

#Q11: Replace the word Coding for Python
print(coding_for_all.replace('Coding', 'Python'))
print()

#Q12: Replace the word to another 
print(coding_for_all.replace('Coding', 'Python').replace('All', 'Everyone'))
print()

#Q13: Split Coding for All using space as the seperator 
print(coding_for_all.split(' '))
print()

#Q14: Split the list by the commas
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(','))
print()

#Q15: Character at a certain index
coding_for_all = "Coding For All"
print(coding_for_all[0])
print()

#Q16: Last index of 'Coding For All'
print(len(coding_for_all)-1)
print()

#Q17: Character at index 10
print(repr(coding_for_all[10])) #the character is space
print()

#Q18: Acronym for Python For Everyone
python_for_all = "Python For All"
coding_list = python_for_all.split(' ')
for string in coding_list:
    print(string[0], end ='')
print()
print()

#Q19: Acronym for Coding for All
coding_for_all = "Coding For All"
coding_list = coding_for_all.split(' ')
for string in coding_list:
    print(string[0], end ='')
print()
print()

#Q20: Index of first occurence of C 
print(coding_for_all.index('C'))
print()

#Q21: Index of first occurence of F
print(coding_for_all.index('F'))
print()

#Q22: rfind of last occurence of I
print(coding_for_all.rfind('I'))
print()

#Q23: finding 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print()

#Q24: finding last occurence of 'because'
print(sentence.rindex('because'))
print()

#Q25: slice out 'because because because'
print(sentence.replace('because because because ', ''))
print()

#Q26: finding because because because again?
print(sentence.find('because'))
print()

#Q27: is a repeat... i am not doing it

#Q28: 'Coding For All' start with Coding
print(coding_for_all.startswith('Coding'))
print()

#Q29: 'Coding For All' end with coding
print(coding_for_all.endswith('coding'))
print()

#Q30: remove the trailing spaces
coding_for_all = '  Coding For All      '
print(coding_for_all.strip())
print()

#Q31: which is true
print('30DaysofPython'.isidentifier())
print('thirty_day_of_python'.isidentifier())
print()

#Q32: join a list
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))
print()

#Q33: Use new line escape sequence
print('I am enjoying this challenge \nI just wonder what is next')
print()

#Q34: Use new tab escape sequence
print('Name\tAge\tCountry\tCity\nAsabenth\t250\tFinland\tHelsinki')
print()

#Q35: String formatting
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {:.0f} meters square'.format(radius, area))
print()