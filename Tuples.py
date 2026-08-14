#tuples and lists does not contain unique
fruits = ('mango', 'banana', 'apple', 'orange', 'pineapple')
ListFruits = list(fruits)
Name = 'Exequiel', 2, True, ['Ab', 'bc', 1], (1, 2, True)

print(fruits)
print(Name)
newName = list(Name)
newName[3][0].pop()
newName.append('heyhey')
Name = tuple(newName)
print(len(Name))

fruits = 'tomato', 'apple', 'banana', 'tomato', 'okra'
x = list(fruits)
x.insert(3,'papaya')
fruits = tuple(x)

XY = Name + fruits
print(XY)
Y = fruits.index('tomato')
print(Y)
'''
fruits = 'apple', 'tomato', 'banana', 'tomato',

name = 'Exequiel',

print(fruits[0])


#1
odd = []
#2 and #3
start = int(input('Enter your first number: '))
end = int(input('Enter your last number: '))
end += 1
#5
if start % 2 == 1:
    start += 1
    for TmpVar in range(start,end,2):
        odd.append(TmpVar)
#    print(odd)
#4
elif start % 2 == 0:
    for TmpVar in range(start,end,2):
        odd.append(TmpVar)
#    print(odd)

#6 #7 #8 #9
oddNum = tuple(odd)
print(oddNum)
print(str(odd[0]) + ' and ' + str(odd[-1]))
#10
print(len(oddNum))


#1
List_even = []
#2 and 3
fnum = int(input('Second number must be greater than first number.\nEnter first number: ').strip())
lnum = int(input('Enter second number: ').strip())
#4 and 5
for x in range(fnum,lnum,2):
    if fnum % 2 == 0:
        List_even.append(x)
    if fnum % 2 == 1:
        fnum += 1
        List_even.append(fnum)
        fnum += 1


#6 7 8 9
tuple_even = tuple(List_even)

print(List_even)
print(tuple_even)
print(str(List_even[0]) + ' and ' + str(List_even[-1]))
print(len(List_even))
'''

















