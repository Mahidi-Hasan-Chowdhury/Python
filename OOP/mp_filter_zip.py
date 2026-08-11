a = ["Mahidi","Siam","Asif"]

for i in a:
    print(len(i))


lengths = list(map(len,a))    
print(lengths)

temp_cel = [0,20,30,35]
def converter(b):
    far = (b * 9/5)+32
    return far

for i in temp_cel:
    print(converter(i))


temp_far = list(map(converter, temp_cel))    
print(temp_far)

far = list(map(lambda x: (x*9/5)+32, temp_cel))
print(far)


m = [35,80,80,12,49]
passed = list(filter(lambda x: x>=40, m))
print(passed) 


# Zip
name = ['Red', 'Green', 'Blue']
mark = [12,90,42]
result = list(zip(name,mark))
result2 = list(zip(mark,name))
print(result)
print(result2)