def doubled(x):
    return x*2

result = doubled(10)
print(result)

tripled = lambda num : num*3
triple = tripled(10)
print(triple)

add = lambda x,y : x+y
sum = add(11,13)
print(sum)

numbers = [1,2,3,4,5]
doubled_num = map(doubled,numbers)
squared = map(lambda x:x*x,numbers)
print(list(doubled_num))
print(list(squared))

actors = [
    {'name':'Mahidi','age':21},
    {'name':'Rahid','age':30},
    {'name':'Asif','age':32}
]

juniors = filter(lambda actor: actor['age']<=30,actors)
fivers = filter(lambda actor: actor['age']%5==0,actors)

print(list(juniors))
print(list(fivers))