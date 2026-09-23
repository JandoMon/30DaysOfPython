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
print('Q14:Join the IT companies with #;')
print('#; '.join(it_companies))
print()

#Q15: Check if a certain company exists in the IT companies list
print('Q15:Check if a certain company exists in the IT companies list')
does_exist = 'APPLE' in it_companies
print(does_exist)
print()

#Q16: Sort the list using sort()
print('Q16:Sort the list using sort()')
sorted_list = sorted(it_companies)
print(sorted_list)
print()

#Q17: Reverse the list
print('Q17: Reverse the list')
reverse_list = sorted(sorted_list,reverse=True)
print(reverse_list)
print()

print(it_companies)
print()
#Q18: Slice out the first three companies
print('Q18: Slice out the first three companies')
first_three = it_companies[3::1]
print(first_three)
print()

#Q19: Slice out the first three companies 
print('Q19: Slice out the last three companies')
last_three = it_companies[:-3:1]
print(last_three)
print()

#Q20: Slice out the middle of the companies 
print('Q20: Slice out the middle of the companies')
middle_three = it_companies[3:6]
print(middle_three)
print()

#Q21: Remove the first company 
print('Q21: Remove the first company of the list')
del it_companies[0]
print(it_companies)
print()

#Q22: Remove the middle company
print('Q22: Remove the middle company')
middle_index = int((len(it_companies)-1)/2)
del it_companies[middle_index]
print(it_companies)
print()

#Q23: Remove the last company
print('Q23: Remove the last company')
del it_companies[len(it_companies)-1]
print(it_companies)
print()

#Q24: Remove the whole list
print('Q24: Remove the whole list')
it_companies.clear()
print(it_companies)
print()

#Q25: Destroy the IT company list
print('Q25: Destroy the IT company list')
del it_companies
print('it_companies is destroyed')
print()

#Q26: Join the two list
print('Q26: Join the two list')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end)
print(back_end)
front_end.extend(back_end)
print(front_end)
print()

#Q27: make fullstack
print('Q27: Make a fullstack list')
fullstack = front_end.copy()
index_redux = fullstack.index('Redux') +1
fullstack.insert(index_redux, 'Python')
fullstack.insert(index_redux + 1, 'SQL')
print(fullstack)
print()

#LVL2: DO IT
print('LEVEL TWO ACTIVATED')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

sorted_ages = sorted(ages)
print(sorted_ages)

youngest = sorted_ages[0]
oldest = sorted_ages[len(sorted_ages)-1]
min_max = youngest + oldest
print(min_max)

middle_list = int((len(sorted_ages)-1)/2)
middle_age = sorted_ages[middle_list]
print(middle_age)

average = sum(ages) / len(ages)
print(average)

range = oldest - youngest
print(range)

print(round(abs(youngest - average),2))
print(round(abs(oldest - average),2))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
middle_index_countries= int((len(countries)+1)/2)
print(countries[middle_index_countries])
print(countries[:middle_index_countries])
print(len(countries[:middle_index_countries]))
print()
print(countries[middle_index_countries:])
print(len(countries[middle_index_countries:]))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_world = countries[:3]
scandic = countries[3:]
print(first_world)
print(scandic)


