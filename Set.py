num_set = {1, 2, 3, 6, 8}
empty_set = set()
letter = {'a', 'b', 'x', 'y', 1, 2, 3, 6, 8}

new = num_set | empty_set
_2ndmethod = letter.union(num_set).union(empty_set)

# print(_2ndmethod, new)
#
#
# difference1 = num_set - letter
difference2 = letter - num_set
#
# print(difference1)
#print(difference2)
#
# print(letter >= num_set)
# print(letter)
#
#
# difference1 = num_set - letter
# difference2 = letter.difference(num_set)
# print(difference1)
# print(difference2)


dif1 = letter.symmetric_difference(num_set)
dif2 = num_set.symmetric_difference(letter)

print(dif1)
print(dif2)

user_string = input('Enter something: ').strip()
inputset = set()

inputset.update(user_string)

print((inputset))



input1 = input('What\'s on your mind?')
input2 = input('What\'s on your mind yesterday?')

set1 = set()
set2 = set()

set1.add(input1)
set2.add(input2)

# unyon1 = set1 | set2
# int1 = set1 & set2
# setdiff1 = set1 - set2
# setdiff2 = set2 - set1
# symdiff1 = set1 ^ set2
# symdiff2 = set2 ^ set1
#
#
setA = {10, 20}
setB = {10, 20, 30, 40}
setC = {50, 60}

# 1. Is setA a subset of setB?
print(setA <= setB)
# 2. Is setB a proper superset of setA?
print(setB < setA)
# 3. Is setA disjoint with setC?
print(setA.isdisjoint(setC))
# 4. Is setB a superset of setA?
print(setB >= setA)
# 5. Is setA a proper subset of setB?
print(setA < setB)

