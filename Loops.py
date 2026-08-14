warriors = ["Curry", "Thompson", "Green"]
food = ['Teriyaki', 'Sisig', 'Chicken']
food_warrior = warriors[0:2] + food[:4]

print(food_warrior)


for tmpVar in warriors:
   if tmpVar == 'Thompson':
       continue
   print(tmpVar)
else:
   warriors.append('Lebron')
   print(warriors)


for f in food:
   if f == 'Teriyaki':
       break
   print(f)

for alpha in range(3):
   print(warriors)

for x in warriors:
   for y in food:
       print(x + y)

for tmpVar in warriors:
   if tmpVar == "Thompson":
       break
   print(warriors)




#odd.append(1)


odd1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
odd = []
even = []


for tmpVar in range(0,31,2):
   even.extend([tmpVar])
else:
   print(even)

for x in range(1,31,2):
   odd.extend([x])
else:
   print(odd)


#name = input('What\'s your name: ')


bits = int(input('Please enter number of bits: '))
for x in range(bits):
    y = 2**x
    print('\n2 raised to ' + str(x) + ' = ' + str(y))

fruits = ['apple', 'banana', 'mango', 'orange']

for x in fruits:
    print(x)



















