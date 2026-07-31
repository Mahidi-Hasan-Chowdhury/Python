# num = 1;
# while num <= 10:
#     print(num)
#     num += 1
#     if num == 5:
#        break



# number = 1
# while number<=10:
#     number = number+1
#     if number == 5:
#       continue
# print(number)



numbers = 0
while numbers<=10:
    numbers = numbers+1
    if numbers % 2 ==1:
      continue
    print(numbers)



# For loop in python

number = [5,10,15,20,25]
sum = 0;
for num in number:
   print(num)
   sum = sum+num
   if sum>20:
      print("big number");
print(sum);

text = "Mahidi Hasan Chowdhury"
for char in text:
   print(char)

for i in range(11,19,2):
   print(i)


print("Using f")
my_array = [10, 20, 30, 40, 50]

# Using enumerate() to get both index and value
for index, value in enumerate(my_array):
    print(f"Index: {index}, Value: {value}")

# Using a range() to iterate over indices
for i in range(len(my_array)):
    print(f"Index: {i}, Value: {my_array[i]}")


print("Without f")
my_array = [10, 20, 30, 40, 50]

for index, value in enumerate(my_array):
    print("Index: " + str(index) + ", Value: " + str(value))

my_array = [10, 20, 30, 40, 50]

for i in range(len(my_array)):
    print("Index: " + str(i) + ", Value: " + str(my_array[i]))


print("Using str.format")
for i in range(len(my_array)):
    print("Index: {}, Value: {}".format(i, my_array[i]))


print("Using % operator")
for i in range(len(my_array)):
    print("Index: %d, Value: %s" % (i, my_array[i]))
