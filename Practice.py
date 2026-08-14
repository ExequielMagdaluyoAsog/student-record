#Different variables declaration & Operators

_apple=13
firstname ="exequiel"
print(firstname)
firstname = "Asog"
print(firstname)
Bul=True
print(Bul)

Num2=25
Num1=2
Num3=4


div1=Num2//Num3
print(Num2*Num1)

print(Num2 + Num1)
print(25//5)
print(div1)

NumEx= Num3 ** Num2
print(4**5)
print(Num3 ** Num2)
print(NumEx)

#Module Operator = %, return the remainder
module1=Num2%Num3
print(module1)
print(25%4)


num1=8
num2=7
num3=25
sum1=num1 + num2 + num3
prod1=num1 * num2
div1=num3 / num2
mod1=num3 % num2
int1=num3 // num1

print(sum1, prod1, div1, mod1, int1)
print(num1 + num2 + num3)
print(8 * 7)

#String
fname = "exequiel "
lname = "asog"
age = "24"
agee = 25


print("Exequiel," + str(31))
fullname = fname + lname + str(agee)
print(fname + lname + str(agee))
print(fullname)

num1 = 15
num2 = 7
num3 = 8
sum = num1 + num2 + num3
quotient = num1 // num2
remainder = num1 % num2

print("The sum of 15, 7, and 8 is " + str(sum))
print("The sum of " + str(num1) + ', ' + str(num2) + ", and "  + str(num3) + ' is ' + str(sum))
print("The sum of" + str(num1)+"," + str(num2)+"," + "and" + str(num3) + "is" + (sum))
print("The sum of" +" " + "15, 7, 8, is" + print(sum))
print("15 divided by 7 equals " + str(quotient) + " remainder " + str(remainder))
print(str(num1) + " divided by " + str(num2) + " equals " + str(quotient) + " remainder "\
    + str(remainder))

#Getting input from users

name = input("What's your name?")
print("hello " + str(name) + '!')

input("How old are you? ")

firstname = input("Firstname: ")
num1 = input("Give a number: ")
num2 = input("Give another number: ")

print("Thanks, " + firstname)
print("Your number inputs are " + str(num1) + ' and ' + str(num2))

#Exercises - VARIABLES AND OPERATIONS
#Fishball (1 stick) /20php

order = float(input('\nPrice:\nFishcake (1 stick) / 20php\nHow many stick/s of fishcake do you want? '))
cash_on_hand = float(input('How much is your money? '))

bill = order * 20
change = (cash_on_hand) - (bill)

print('\nTotal fishcake order: ' + str(bill) + 'php')
print('Change: ' + str(change) + ' php')

fname = input('What\'s your name? ')
num1 = int(input('Give me a number: '))
num2 = int(input('Give me another number: '))

_sum1 = num1 + num2
_product = num1 * num2

print("\nHi " + fname + ',')
print('You entered ' + str(num1) + ' and ' + str(num2))
print('The sum of the 2 number are: ' + str(_sum1))
print('The product of the 2 numbers are: ' + str(_product))


exrate = float(input('\nMagkano ang 1 PHP to KRW ngayon? '))
phpAmount = float(input('How many PHP do you want to convert? '))

Korean_Value = phpAmount * exrate

print(str(phpAmount) + ' php = ' + str(Korean_Value) + ' krw')

############
exrate_japan = float(input('\nMagkano ang 1 PHP to Japanese Yen ngayon? '))
phpAmount_2 = float(input('How many PHP do you want to convert? '))

JPY_Value = phpAmount_2 * exrate_japan

print(str(phpAmount_2) + ' php = ' + str(JPY_Value) + ' jpy')
############
exrate_usd = float(input('\nMagkano ang 1 PHP to USD ngayon? '))
phpAmount_3 = float(input('How many PHP do you want to convert? '))

USD_Value = phpAmount_3 * exrate_usd

print(str(phpAmount_3) + ' php = ' + str(USD_Value) + ' usd')


fname = input('What\'s your firstname? ')
lname = input('What\'s your last name? ')
birth = input('Year of birth? ')

birth_compute = 2025 - int(birth)

print('\nFull Name: ' + fname, lname)
print('Age: ' + str(birth_compute))

Exam_fee = float(input('\nHow much is CCNA Exam fee (USD): '))
exrate = float(input('1 USD to PHP exchange rate: '))

cost = Exam_fee * exrate
VatCompute = (cost * .12) + cost

print('\nCCNA Exam fee is: ' + str(VatCompute) + ' PHP with 12% tax')

second = int(input('\nNumber of seconds: '))
hour_compute = second // 3600
minute_compute = (second % 3600) // 60
second_compute = second % 60


print( '\n' + str(second) + ' second/s is: \n')
print(str(hour_compute) + ' hour/s, ' + str(minute_compute) + ' minute/s and ' \
     + str(second_compute) + ' seconds')


Number_sec = int(input('\nNumber of seconds: '))

sec = Number_sec % 60

minutes1 = (Number_sec // 60) % 60
hr = (Number_sec // 3600) % 24
day = (Number_sec // 3600) // 24

print('\n' + str(Number_sec) +  ' second/s is:' )
print('\n' + str(day) + ' day/s', str(hr) + ' hr/s,', str(minutes1) + ' min/s, and', str(sec) + ' second/s')


#IF-ELSE Exercises
num1 = float(input('\nGive me a number: '))
num2 = float(input('Give me another number: '))

if num2 > num1:
   print('\n' + str(num2) + ' is greater than the other number ')
elif num2 < num1:
   print('\n' + str(num2) + ' is less than the other number ')
else:
   print(str(num2) + ' = ' + str(num1))
# Konting logic, may mali sa ginawa if d napalabas ung output
# longer for some readers to parse the logic



temp = float(input('\nWhat\'s your temperature check (Celsius)? '))

if temp <= 36.9:
   print('\n' + str(temp) + ' Degree Celsius is allowed to enter ')
else:
    print(str(temp) + ' Degree Celsius is NOT allowed to enter')


birth = int(input('\nYear of birth: '))


if birth >= 1997 and birth <= 2012:
    print('Gen Z')
elif birth >= 1981 and birth <= 1996:
    print('Millennials')
elif birth >= 1965 and birth <= 1980:
    print('Gen X')
elif birth >= 1946 and birth <= 1964:
    print('Boomers')
elif birth >= 1928 and birth <= 1945:
    print('Silent')
else:
    print('undefined year')

ave = int(input('\nInput your grade in %: '))

if ave < 75 :
   print('\nGrade: 5 or failed')
elif ave >= 75 and ave <= 79:
   print('\nGrade: 3')
elif ave >= 80 and ave <= 84:
   print('\nGrade: 2.50')
elif ave >= 85 and ave <= 89:
   print('\nGrade: 2.00')
elif ave >= 90 and ave <= 97:
   print('\nGrade: 1.50')
elif ave >= 98 and ave <= 100:
   print('\nGrade: 1\nYour a dean\'s lister. Congrats!\nTuition Fee is \
   100% free')
#Catch all
else:
   print('Choose number from 60 - 100 only or Invalid number')


grade = float(input('\nInput your grade in %: '))

if grade == 100:
    print('Grade: 1')
elif grade <= 99 and grade >= 94:
    print('Grade: 1.5')
elif grade <= 93 and grade >= 88:
    print('Grade: 1.75')
elif grade <= 87 and grade >= 82:
    print('Grade: 2')
elif grade <= 81 and grade >= 76:
    print('Grade: 2.5')
elif grade == 75:
    print('Grade: 3')
elif 60 <= grade <= 74:
    print('Grade: 5')
else:
    print('Invalid number!')


birthyear = int(input('\nBirth year: '))

if birthyear >= 1946 and birthyear <= 1964:
   print('\nYou\'re a Baby Boomer')
elif birthyear >= 1965 and birthyear <= 1980:
   print('\nYou\'re a Generation X')
elif birthyear >= 1981 and birthyear <= 1996:
   print('\nYou\'re a Millenial')
elif birthyear >= 1997 and birthyear <= 2015:
   print('\nYou\'re a Gen Z')
elif birthyear >= 2016 and birthyear <= 2025:
   print('\nYou\'re a Gen Alpha')
else:
   print('Cannot Identify you\'re generation' )


#List and methods like insert, append, extend, etc
food = ['Oily Food', 'Carbs', 'Sweets', 'Fast food', 'Pork']
presidents = ['marcos', 'cory', 'ramos', 'erap']
presidents.append(5)
presidents.extend([6, 7, 8, 9, 10])
newlist = presidents[4:]
name = 'exequiel'
food.insert(4, 'Beef')
print(food)
newName = name[0]
print(newName)
newlist = presidents[:2]
print(newlist)

print(len(presidents[4:]))

presidents[3] = "Joseph Estrada"

food[0] = 'Oily Foodssss'
presidents.insert(3,'Rodrigo Duterte')

food.insert(3,'Rodrigo Duterte')

print(presidents)

#Capital Letter comes first in sort() method
newlist.sort(reverse=False)
print(newlist)
presidents.pop(1)
del food[2]
food.clear()
del food

presidents.insert(6, 'Best')

print(presidents)

Showtime = ['Vice Ganda', 'Anne Curtis', 'Vhong Navarro']
EB = ['Vic Sotto', 'Tito Sotto', 'Joey De Leon']
num = [1, 2, 3, 4]
newlist = Showtime + num


Heat = []
print(Heat)
Heat.append('Iguodala')
Heat.extend(['Herro', 'Adebayo', 'Dragic', 'Butler'])
Heat.insert(3, 'Crowder')
print(Heat)
Heat.pop(2)
Heat.insert(2, 'Olynyk')
print(Heat)
Heat.sort(reverse=False)

print(Heat)

name = 'exequiel'
x = name[3].upper()
y = name[]
print(x)
print(name)

ans = input('Yes or NO? ')

print(1/2)
print(2**0)
odd = []

for x in range(1,31,2):
   odd.append(x)

print(odd)

name = 'exequiel'
new_name = list(name)
print(new_name)

alphanumeric = 'exeqa1241AB'
alphanumeric_list = list(alphanumeric)
print(alphanumeric_list)

alphanumeric_list.sort(reverse=False)
print(alphanumeric_list)



print(24)
print(25*5)
print(True)
print("""
#      Hi, What's your name?
#      How old are you?"\nThat's right!
""")

# print function like learning how to print using printer to produce output then troubleshooting/etc
print("haller")
print("hello")

print('''
"Hard evidence isn't hard evidence if you don't break your back digging for it.

Grelshch glares at her.
"I got a lead, Dom."

"you got a lead."
''')

print('Nagkita kami kahapon,\n\"Kamusta kana? Isa\'t kalahati din yon ah"')










