# set: unique items collection

numbers = [12,23,34,45,12,23,89]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)

for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 exists')

A = {1,2,3,4}
B = {2,3,5}
print(A&B)
print(A|B)