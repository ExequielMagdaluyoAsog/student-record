'''
students = []
ans = 'Y'

while ans == 'Y':
    studentInput = input('\nEnter Student Name: ')
    students.append(studentInput)

    ans = input('\nAdd another student? YES/NO: ').strip().upper[0]

    while ans not in ['Y', 'N']:
        print('Invalid answer! Please type Yes or No only.')
        ans = input('\nAdd another student? YES/NO: ').strip().upper[0]

for y in students:
    print(y)


#    x = input('Do you want to input another student? ')
#    ans = x.upper()
#    if x == 'Y'


# while ans == y:
#    students =+ list
#    input('Enter Student Name: ')
# print(students)

# ans = input('Do you want to add student? Y/N ')
# StudName = input('Enter Student Name: ')


#studentInput = input('Enter Student Name: ')
#students.append(studentInput)

#students = input('Enter Student Name: ')


'''
ABC = ['Exequiel', 2, True, ['Ab', 'bc', 1], (1, 2, True)]

# ABC.insert(1,'mamba')
# print(ABC)
#
# name = '23456789exequiel magdaluyo asog 31 male philippines33'
# print(name.count('e'))
#
# B = name.count('0')
# print(B)
#
#
#
# i = 0
# while i != 9:
#     B = name.count('1')
#     print(B)
#     i += 1
#
# sample = input('Enter something: ')
# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#
# for tmp_var in num:
#     if tmp_var in sample:
#         print('String have number/s')
#         break
# else:
#     print(f'Does not have numbers in {sample}')


# print('############################################################')
# sample1 = input('Enter something: ')
# splitted = list(sample1)
# i = "0123456789"
#
#
# if any(x in i for x in sample1):
#      print('String have number/s \nPlease try again.')
# else:
#     print('Does not contain numbers')































