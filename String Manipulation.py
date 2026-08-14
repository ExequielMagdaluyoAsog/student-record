Name = 'Exequiel Magdaluyo Asog'

#Where exactly the strings in terms of counting
x = Name.index('x')
print(x)

#slicing
print(Name[x+1:])

#Removing string
print(Name.strip('Exequiel '))

#input function
TmpVar = input('What\'s your name: ').upper()
print(TmpVar)

TmpVar1 = input('What\'s your name: ').lower().strip()
print(TmpVar1)

TmpVar2 = input('What\'s your name: ').capitalize()
print(TmpVar2)

Name = 'exequiel Magdaluyo Asog'

AB = Name.replace('e','3',2).replace('x','X')
print(AB)

FName = input('\nEnter your firstname: ').strip().capitalize()
LName = input('Enter your lastname: ').strip().capitalize()

print('##########################################################################')
print('Dear ' + FName + ',\n')
print('We created a new email account for you, Here are the details: ')
print(FName + LName + '@mnet-it.com')
print('Your default password is: ' + FName[:2].lower() + LName[:2].lower() + '1234\n')
print('We\'re happy to have you onboard ' + FName)


Email = 'Dear $,\n\nWe created a new email account for you, Here are the details:\n \
    $%@mnet-it.com\n\nYour default password is: XZ1234\n\nWe\'re happy to have you onboard $!'

Email = '''
Dear <FName>,

We created a new email account for you, Here are the details:
    <FName>%@mnet-it.com

Your default password is: XZ1234

We\'re happy to have you onboard <FName>!

xoxo
'''


fname = input('Enter your firstname: ').strip().capitalize()
lname = input('Enter your lastname: ').strip().capitalize()

password = str(fname[:2]).lower() + str(lname[:2]).lower() + str('1234')

print(f'''
Dear {fname},

We created a new email account for you, Here are the details:
{fname}{lname}@mnet-it.com
Your default password is: {password}

We're happy to have you onboard {fname}
''')


NewEmail = Email.replace('<FName>', FName).replace('%', LName).replace('X', FName[:2].lower()) \
   .replace('Z', LName[:2].lower())

print(NewEmail)


Name = input('What\'s your favorite NBA Team: ')
#Len function
Str = input("Please type something: ")
X = len(Str)
print(X)


FName = input('What\'s your first name: ').capitalize()
LName = input('Lastname: ').capitalize()

AutoReply = '''
Hi <FName> <LName>,

So happy to see you here <FName>

Till Next time.
'''
print(AutoReply.replace('<FName>',FName).replace('<LName>',LName))

StringOnly = input('Enter something: ')

samp = 'exe123'

AB = '1' in samp
print(AB)

fruits = ["apple", "banana", "cherry"]

item = "banana"

if item in fruits:
   index = fruits.index(item)
   print(f"Found at index: {index}")
else:
   print("The item was not found in the list.")

#name = 'exe44'

#A = '4' in name
#print(A)

'''
#pw = input('\nEnter password: ').strip()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

A = 0
while A == 0:
    pw = input('\nEnter password: ').strip()
    for pw_letter in alphabet:
        if pw_letter in pw.upper() and len(pw) >= 8:
            break
##############################################################################
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
var1 = True

while var1:
    passwd = input('\nEnter password: ').strip()
    for temp1 in letter:
        if temp1 in passwd and len(passwd) >= 8:
            print('Pw successfully created!')
            var1 = False
            break
######################################################################################
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
var1 = True

while var1:
    passwd = input('\nEnter password: ').strip()
    for temp1 in letter:
        if temp1 in passwd and len(passwd) >= 8:
            print('Pw successfully created!')
#           var1 = False
            break
    else:
        continue
    break
'''
































