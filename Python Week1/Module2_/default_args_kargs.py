def sum(num1,num2,num3=0):
    result = num1 + num2 + num3;
    return result
total = sum(99,11)
print(total)


def sum(*number):
    print(number)
total = sum(1,2,3,4,5)
print(total)


def sum(*number):
    print(number)
    for num in number:
        print(num)
total = sum(1,2,3,4,5)
print(total)


def sum(num1,num2,*number):
    print(number)
    for num in number:
        print(num)
total = sum(1,2,3,4,5)
print(total)


def sum(num1,num2,*number):
    print(number)
    sum = 0
    for num in number:
        print(num)
        sum = sum+num
    return sum
total = sum(1,2,3,4,5)
print(total)

