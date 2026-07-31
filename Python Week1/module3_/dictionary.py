numbers = [12,23,34,45,56,67]

person = ['Mahidi','B.baria',23,'student']

# key value pair
# dictionary
# object
# hash table
# overlap with set

person = {'name':'Mehedy','address':'B.baria','age':21, 'Job': 'student'}
print(person)
print(person['Job'])
print(person.keys())
print(person.values())
person['language'] = 'Python'
person['name'] = 'Mahidi'
del person['age']
print(person)


for item in person:
    print(item)

for key,value in person.items():
    print(key,value)
