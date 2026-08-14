########################################################################################################################
'''
print('##############################################################')
FirstNum = int(input('\nBefore proceeding, second number must \
be greater than your first number.\n\nPlease input your first number: '))
SecondNum = int(input('Please input your second number: '))
print('##############################################################')
print('\nCounting even numbers...')

x = FirstNum % 2
if x == 1:
    FirstNum += 1

while FirstNum <= SecondNum:
    print(str(FirstNum))
    FirstNum += 2
else:
    print('##############################################################')
###################################
for x in range(first, second,2):
    even = first % 2
    if even == 0:
        print(x)
    else:
        x +=1
        print(x)
print(x + 2)

'''
########################################################################################################################
#startrange = int(input('\nBefore proceeding, second number must \
#be greater than your first number.\n\nPlease input your first number: '))
#endrange = int(input('Please input your second number: '))
#print('\nCounting even numbers...')

#if (startrange % 2) == 0:
#    print(startrange)
#    while startrange < endrange:
#        startrange += 2
#        print(str(startrange))
#elif (startrange % 2) > 0:
#    startrange += 1
#    while startrange < endrange:
#        print(str(startrange))
#        startrange += 2

'''

students = []

while True:
    student_name = input('\nEnter your student name: ').strip().capitalize()
    students.append(student_name)

    while True:
        choice = input('Do you want add another student name? YES/NO ').strip().upper()

        if choice[:3] == 'YES': # Use startswith() method
            break
        elif choice[:2] == 'NO':
            print('\nStudent list updated...')
#            A = False
            break #exits the validation
        else:
            print('\nPlease enter YES or NO only')
#            continue

    if choice[:2] == 'NO': # Use startswith() method
        break

while True:
    should_print = input('Do you want to print the student names? Y/N ').strip().upper()

#use startswith method and do not use variable x, instead use actual variable like student
    if should_print[:3] == 'YES':  # Use startswith() method
        for x in students:
            print(x) #Descriptive and lowercase like student or student_list
#        else:
        break
    elif should_print[:2] == 'NO': # Use startswith() method
        print('\nHave a nice day ahead!')
        break
    else:
        print('\nPlease enter YES or NO only')
#        continue


#It can scale to storing more information per student (Age, Grades)
#Handles errors if enter numbers as a name
##########################################################################
#1
stud = []
#2
ans = 'Y'
while ans == 'Y':
    Input = input('\nEnter Student Name: ')
    stud.append(Input)

#3
    x = input('\nAdd another student? YES/NO: ').upper().strip()
    ans = x[0]
    while ans not in ['Y', 'N']:
        print('Invalid answer! Please type Yes or No only.')
        x = input('\nAdd another student? YES/NO: ').upper().strip()
        ans = x[0]
print('###################################\nStudent list updated...\n')
for y in stud:
    print(y)
'''
########################################################################################################################
'''

#4 - Create an Improved UX in your code where user doesn't need to type again correct inputs.

odd_numbers = []

Gate_1 = 'Lock'
while Gate_1 == 'Lock':
    start = input('Enter the start of a range: ').strip()
    end = input('Enter the end of a range: ').strip()

    if start.isdigit() and end.isdigit():
        start, end = int(start), int(end)

        if start % 2 == 0:
            start += 1

        if start <= end:
            for num in range(start, end + 1, 2):
                odd_numbers.append(num)
            Gate_1 = 'Tuple created'
        else:
            print('\nFirst number should be lower than the other number.\n')
    else:
       print('\nIt must be a number. Please try again.')


odd_number_tuple = tuple(odd_numbers)

print(f"""
Tuple: {odd_number_tuple}

First number of a tuple: {odd_number_tuple[0]}
Last number of a tuple: {odd_number_tuple[-1]}
Number of items index of a tuple: {len(odd_number_tuple)}
""")

#Improved UX and accepting negative integers.

def get_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid number.")

start = get_number("Enter the start of a range: ")
end = get_number("Enter the end of a range: ")

if start % 2 == 0:  # ensure odd start
    start += 1

if start <= end:
    odd_numbers = list(range(start, end + 1, 2))
    odd_number_tuple = tuple(odd_numbers)

    print(f"""
    Tuple: {odd_number_tuple}

    First number of a tuple: {odd_number_tuple[0]}
    Last number of a tuple: {odd_number_tuple[-1]}
    Number of items in tuple: {len(odd_number_tuple)}
    """)
else:
    print("Start must be less than or equal to end.")







'''
########################################################################################################################

'''
num = "0123456789"
User1 = input('Enter new password: ')
#list1 = list(User1)

while (
        len(User1) <= 8
        or not any(x in User1 for x in num)
):
    User1 = input('Enter new password: ')
else:
    print(f'Password successfully created {User1}')


num = "0123456789"
User1 = input('Enter new password: ')
#=list1 = list(User1)

#Repeat if pw not properly set
while (
    len(User1) <= 8
    or not any(x in num for x in User1)
    or User1.isdigit()
):
    User1 = input('Enter new password: ')
#else done
else:
    print(f'Password successfully created "{User1}"')
'''



# #make this a standard code
# #wrap the logic in a function and use a rule-driven design (list of checks)
#
# from getpass import getpass
# # def get_number(prompt):
# #     while True:
# #         value = input(prompt).strip().capitalize()
# #
# #         if value.isalpha():
# #             return value
# #         else:
# #             print('\nPlease enter a valid name.')
# #
# #
# # fname = get_number('Enter your firstname: ')
# # lname = get_number('Enter your lastname: ')
# #
# # email_address = '#'
# # while '@' not in email_address :
# #     email_address = input('Enter your email address: ').strip()
# #
# #     if '@' not in email_address:
# #         print('\nNot a valid email address. Please enter a valid email.')
# #
# while True:
#     #
#     password = getpass('Enter your password: ').strip()
#     check_num = any(num.isdigit() for num in password)
#     check_letter = any(letter.isalpha() for letter in password)
#
#     if len(password) < 8:
#         print('\nPassword must be at least 8 characters.')
#     elif not check_letter:
#         print('\nPassword must have at least 1 letter')
#     elif not check_num:
#         print('\nPassword must have at least 1 number')
#     else:
#         print('\nPassword has been created.')
#         break
#
# pass_hidden = password[0] + (len(password)-2) * '*' + password[-1]
# #
# # print(f'''
# # Thanks for ur registration, {fname}
# #
# # Here are your registration details:
# #
# # First Name: {fname}
# # Last Name: {lname}
# # Email Address: {email_address}
# # Password: {pass_hidden}
# # ''')















