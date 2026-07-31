def multiple():
    return 3,4
print(multiple())

things = 'pen','tripod','pc','phone','web cam', 'charger'
print(things)
print(things[0])
print(things[-2])
print(things[3:6])

if 'phone' in things:
    print('exists')

for item in things:
    print(item)

print(len(things))

number = (1,2,3)
print(number)

mega = ([2,3,4],[1,2,3,4])
mega[0][1] = 666
print(mega)
#tuple can't be changed. but if tuple has mutable things inside then you can change the tuple.