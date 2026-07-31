numbers = [12,45,98,68]
numbers.append(23)
print(numbers)
numbers.insert(2,71)
print(numbers)
if 98 in numbers:
   numbers.remove(98)
if 8 in numbers:
   numbers.remove(8)

print(numbers)    

last = numbers.pop()
print(last,numbers)

if 45 in numbers:
   index = numbers.index(45)
   print(index)

numbers.reverse()
print(numbers)