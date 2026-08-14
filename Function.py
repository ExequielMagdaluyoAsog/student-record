# def bill(kuryente, wifi, rent, food):
#     Total_bills = kuryente + wifi + rent + food
#     return Total_bills
#
#
# print(bill(1700, 500, 5500, 4000))
# print('##############################################################')
#
# def email():
#     print('This is a simple function')
#     print('This is a simple function')


# def my_print(name):
#     print(name)
#
# #data types
# cars = ['toyoto', 'yahama', 'honda']
# my_print(cars)

# def sumOf2Values(Name1, Name2):
#     Sum = Name1 + Name2
#     print('First value is ' + str(Name1))
#     print('Second value is ' + str(Name2))
#     print('Sum = ' + str(Sum))
#     return Sum
#
#
# sumOf2Values(5, 2)

#*args | arbitrary args
# def students(*names):
#     print(names)
# #   for x in names:
# #        print(x)
#
# students('exequiel', 'kel', 'kiel')

# set_a = {}
# def fullname1(fname, lname, midname):
#     print(f'first name = {fname}')
#     print(f'last name = {lname}')
#     print(f'Mid name = {midname}')
#
#
#
#
# fullname1('exequiel', 'Asog', 'magdaluyo')
# print()
# #kwargs
# fullname1(fname='Exequiel', midname='magdaluyo', lname='Asog')

#**kwargs | arbitrary kwargs
# def fullname2(**names):
#     print(names)
#     print(f'first name = {names}')
#
# fullname2(Firstname='Exequiel', Lastname='Asog', age=31, occupation='Cloud engineer', Address='Pampanga')

# def fullname3(**names):
#     for key, value in names.items():
#         print(f'{key}: {value}')
#     print('####################################')
#
# fullname3(Firstname='Exequiel', Lastname='Asog', age=31, occupation='Cloud engineer')

# def students_details(**details):
#     print(details.get('lname'))
#
# students_details(fname='kobe', lname='asog', number='24')

#Can retrieve the computations, values from inside to outside
#Not just printing but can use as variables/etc
#Return
def vat_compute(price):
    vat = price * .30
    return vat

BasedPrice = float(input('What is the price? '))
print(vat_compute(BasedPrice))
TotalPrice = BasedPrice + vat_compute(BasedPrice)
print(f'Total price: {TotalPrice}')

#Global and local Variable
#Global Keyword inside Functions
# name = 'exequiel'
# print(name)
#
# def fullname1(fname, lname, midname):
#     global name
#     name = name + ' Asog'
#     print(name)

#Anonymous Functions
# def vat_compute(price):
#     vat = price * .20
#     return vat
#
# print(vat_compute(70000))


# Vat_Compute = lambda price: price * .20
#
# print(Vat_Compute(70000))

# def evenout(lowerlimit, higherlimit):
#     list1 = []
#     if lowerlimit % 2 == 1:
#         lowerlimit += 1
#     for num in range(lowerlimit, higherlimit+1,2):
#         list1.append(num)
#     print(list1)
#
# lowerlimit = int(input('Give me your first number: '))
# higherlimit = int(input('Enter me your first number: '))
#
# evenout(lowerlimit,higherlimit)


def oddout(lowerlimit, higherlimit):
    odd = []
    sum1 = 0

    if lowerlimit % 2 == 0:
        lowerlimit += 1

    for num in range(lowerlimit, higherlimit+1, 2):
        odd.append(num)
        sum1 += num

    print(odd)
    print(f'the sum is: {sum1} ')

    if sum1 % 2 == 0:
        print(f'{sum1} is an even number')
    else:
        print(f'{sum1} is an odd number')

A = int(input('Enter 1st number: '))
B = int(input('Enter 1st number: '))

oddout(A, B)

# def givemewords(stringinput):
#     Count = stringinput.split()
#     return len(Count)
#
# stringinput = input('Please enter any string value: ')
# print(f'input has {givemewords(stringinput)} words')


# def compute(a,b,c,d):
#     return a + b + c + d
#
# electric = float(input('Amount for electric: '))
# wifi = float(input('Amount for Wifi: '))
# rent = float(input('Amount for Rent: '))
# food = float(input('Amount for Food: '))
#
# bill = compute(electric,wifi,rent,food)
# print('Total Bills: ' + str(bill))
# print('Change: ' + str(17000 - bill))



# def greet(x):
#     print(f'hello {x}')
#
# def simple_function():
#     print('hello world')
#     print('')

# def add(a, b, c):
#     print(f'values are: {a}{b}{c}')
#     print(a + b + c)
#
# add(1,2,3)
#
# print(add(1,2,3))

# def grade(Sub1, Sub2, Sub3, Num_Sub):
#
#     ave = (Sub1 + Sub2 + Sub3) / Num_Sub
#     grade = ave * .50 + 50
#     return grade
#
# B = grade(95, 98, 97,  3)

# from Dictionary import add_again
#
# def expenses(*php):
#   return sum(php)
#
# totals = []
#
# choice = 'YES'
# while choice == 'YES':
#     cost = int(input('input your expenses today: ').strip())
#     totals.append(cost)
#
#     choice = add_again('Add another expenses? (YES/NO) ')
#

#Code A
# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner
#
# @changecase
# def myfunction():
#   return "Hello Sally"
#
# print(myfunction())
#
# print('################################################################')
# # Code B
# # simpler, no need for inner function
# def outer(var):
#     def inner():
#       return var().upper()
#     return inner
#
# @outer
# def myfunction1():
#     return "hello world"






################################################################
# def result(grade):
#     def inner():
#         if grade() >= 75:
#             return 'Passed'
#         else:
#             return 'Failed'
#     return inner
#
# @result
# def compute_grade():
#     grado = input('What is your GPA: ').strip()
#     return int(grado)
#
#
#
# print(compute_grade())


def changecase(n):
    def changecase(func):
      def myinner(*kwargs):
          if n == 50:
              case = func(*kwargs).upper()
          else:
              case = func(*kwargs).lower()
          return case
      return myinner
    return changecase


num = int(input('Type 50 if you want a capital letters: ').strip())


@changecase(num)
def myfunction2(continent):
    return continent

country = input('What country do you want to visit: ').strip()

B = myfunction2(country)
print(B)

num = ['apple', 'banana', 'orange', 'zi', 'zae']
name = [1,2,3,4,5,6,7,8]

x = list(map(lambda location:'Parameter didnt use', num))

print(x)

z = list(filter(lambda a:a%2 != 0, name))
print(z)


sorted_name = sorted(num, key=lambda x:len(x))
print(sorted_name)