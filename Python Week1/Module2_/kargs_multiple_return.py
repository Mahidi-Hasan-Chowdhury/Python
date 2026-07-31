#take parameter in order
def full_name(first,last):
    name = f'{first} {last}'
    return name

name = full_name('Mahidi','Hasan')
print(name)


def full_name(first,last):
    name = f'{first} {last}'
    return name
name = full_name(last= 'Mahidi',first='Hasan')
print(name)


#key argument



def a_lot(num1,num2):
    sum = num1+num2
    multi = num1*num2
    subtract = num1-num2
    return sum,multi,subtract
everything = a_lot(55,21)
print(everything)