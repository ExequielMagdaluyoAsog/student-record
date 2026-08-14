'''
notSet = {
    1:'one',
    2:'two',
    3:'Tres',
    4:'Kwatro'
}

try:
    notSet[5]
#   print('\nValue is: ' + str(notSet.get(5)))
except KeyError:
    print(notSet.get(5))
    notSet[5] = 'Singko'
    print('Adding another item in the dictionary...\n...\n...')
    print(str(notSet[5]) + ' is added')
'''
delivery_information = {
    'name': 'Exequiel Magdaluyo',
    'address': 'Pampanga',
    'Contact#': '123',
    'grade': [75, 90, 75]
}

#delivery_information['Civil Status'] = 'Single'
#for key,value in delivery_information.items():
#    print(value)


delivery_information['address'] = 'Taichung, taiwan'
delivery_information['Barangay'] = 'Ginebra'
# print(delivery_information)
delivery_information.pop('Barangay')
#print(delivery_information)
A = delivery_information.keys()
B = delivery_information.values()
C = delivery_information.__sizeof__()
delivery_information.clear()

#elivery_information.items()
#delivery_information['average'] = sum(delivery_information['grade']) / len(delivery_information['grade'])
#del delivery_information
sample = {}.fromkeys('1234','Hello')
student_info = {}.fromkeys(['stu_name', 'stu_info', 'stu_contact'])
student_subject = {}.fromkeys(['Calculus', 'Physics', 'English', 'Programming'],50)
student_subject['Math'] = 101


R1 = {
    'Fa0/0': {
        'Exequiel': {
            'age':'31',
            'Location':'NCR'
        },
        'Subnet Mask':'255.255.255.0'
    },
    'Se0/0': {
        'IP_Add':'172.16.10.1',
        'Subnet Mask':'255.255.255.252'
    }
}
# print(R1['Se0/0']['IP_Add'])
# #print(R1.get('Fa0/0',"Subnet Mask"))
# print(R1['Fa0/0'].get('ey', 'wala'))
'''
login = {'admin': 'admin123', 'user': ['exequiel', 'albern', 'benedict', 'raymond']}

login_prompt = input('Enter your username: ')

if login_prompt not in login['user']:
    print('Invalid access! Please contact your...')


users = {"admin": "1234", "guest": "abcd"}
entered_username = input("Username: ")
print(users.get(entered_username, 'wala ka dito sa list'))

grades = {
    'Anna':[85, 91, 12, 5],
    'Ben':100,
    'Cathy':(100, 102, 200)
}

for name in ["Anna", "Ben", "Cathy"]:
    score = grades.get(name, "No record")
    print(f"{name}: {score}")


sample = {}

Gate1 = True
while Gate1 == True:
    cat = input('Enter category: ')
    val = input('Enter the value of that category: ')
    sample[cat] = val

    while True:
        res = input('Do you want to add another? YES/NO: ')
        if res[0].upper() == 'N':
            Gate1 = False
            break
        elif res[0].upper() == 'Y':
            break
        else:
            print('Invalid answer, type Yes or No only.')


'''
'''
#Student Grades Record
students = []
Gate1 = True
while Gate1 == True:
    fname = input('Please enter the student\'s first name: ').strip().capitalize()
    lname = input('Please enter the student\'s last name: ').strip().capitalize()
    combined = fname + ' ' + lname
    students.append(combined)
    print('Records Updated...')

    while True:
        ques = input('\nAdd another student entry? (Y/N)').strip()
        if ques[0].upper() == 'Y':
            break
        elif ques[0].upper() == 'N':
            Gate1 = False
            break
        else:
            print('Please type Yes or No only!')
subject = []
Gate2 = True
while Gate2 == True:
    sub = input('Enter subject name: ').strip().capitalize()
    subject.append(sub)
    print('Records Updated...')

    while True:
        ques2 = input('Add another subject name entry? (Y/N)')
        if ques2[:1].upper() == 'Y':
            break
        elif ques2[:1].upper() == 'N':
            Gate2 = False
            break
        else:
            print('Please type Yes or No only!')
#Student grades ######on each subject
Grade_dict = {}

for name in students:
    Grade_dict[name] = {}
    print(f'\nFor student {name}: ')
    for sub in subject:
        student_grades = int(input(f'Grade for {sub}: '))
        Grade_dict[name][sub] = student_grades

print('\nStudent Records Updated...\n\nRecords Summary:')
for key in Grade_dict.keys():
    print(key + ':')
    for nested_key, val in Grade_dict[key].items():
        print(nested_key + ': ' + str(val))
    print('')
#print(Grade_dict.values())

'''

#######################################


def ask_name(prompt):
    while True:
        names = input(prompt).strip().title()

        if names and all(name.isalpha() for name in names.split()):
            return names

        print('Invalid name! No numbers and special characters\n')

def ask_subjects(prompt):
    while True:
        value = input(prompt).strip().title()

        if any(subject.isalpha() for subject in value.split()):
            return value
        print('Please enter a valid subject!\n')

def add_again(prompt):
    while True:
        value = input(prompt).strip().upper()

        if value[:2] == 'NO':
            print(''.center(50,'#'))
            return value
        elif value[:3] == 'YES':
            pass
            return value
        else:
            print('Please type YES/NO only!\n')

if __name__ == "__main__":
    student_name = {}
    subjects = {}
    import json

    choice = 'YES'
    while choice == 'YES':
        firstname = ask_name('What is your First Name: ')
        lastname = ask_name('What is your Last Name: ')
        fullname = firstname + ' ' + lastname
        student_name[fullname] = {}
        print('Records Updated...\n'); print(''.center(50,'#'))
        choice = add_again('Add another student entry?: ')

    choice1 = 'YES'
    while choice1 == 'YES':
        subject_name = ask_subjects('Enter Subject Name: ')
        subjects[subject_name] = 50
        print('Records Updated...\n'); print(''.center(50,'#'))
        choice1 = add_again('Add another subjects name entry?: ')


    #Create outer dictionary of names
    #Creates inner dictionary of each subjects with grades
    for name in student_name.keys():
        print(f'\nFor student {name}: ')
        for subject in subjects.keys():
            grade = int(input(f'Grade for {subject}: ').strip())
            student_name[name][subject] = grade

    print('Student Records updated...\n');print('RECORD SUMMARY'.center(50,'#'))
    for name, subject in student_name.items():
        print(f'\n{name}')
        for sub, grade in subject.items():
            print(f'{sub}: {grade}')

    with open(r'C:\Users\exo26\Downloads\student_record.json', 'w', encoding='utf-8') as file:
        json.dump(student_name, file, ensure_ascii=False, indent=2)



#Check improvement on copilot, it can be a mini-project
#Improved category dictionary

# import json
# Categories = {}
#
# def make_category(prompt):
#     while True:
#         value = input(prompt).strip().title()
#         if any(val.isalpha() for val in value):
# #sample.update(value)
#             return value
#
# while True:
#     category = make_category('Enter the category: ')
#     value = make_category('What is the value of that category: ')
# #NOT ABLE to add a list of values in that specific category. It means 1 cat = 1 value only
#     Categories.update({category:value})
# #Continue or exit for printing?
#     while True:
#         add_again = input('\nDo you want to add another category?: ').strip().upper()
#
#         if add_again.startswith('YES'):
#            break
#         elif add_again.startswith('NO'):
#             print(f'Successfully added.....\n{Categories}\n')
#             for cat, val in Categories.items():
#                 print(f'{cat} = {val}')
#             with open(r'C:\Users\exo26\Downloads\categories.json', 'w', encoding='utf-8') as file:
#                     json.dump(Categories, file, ensure_ascii=False, indent=2)
#             raise SystemExit
#         else:
#             print('Please type "YES" or "NO" ONLY')
