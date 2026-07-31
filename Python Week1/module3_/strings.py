name1 = 'Mahidi'
name2 = "Mahidi"
name3 =  """Mahidi Hasan
Chowdhury
"""
name = 'Sakib\'s Khan' #escape\
print(name)
#print(name1)
print(name2)
print(name3)

for char in name3:
    print(char)

print(name2[3])
print(name3[13])
print(name3[-3])
print(name3[::-1])
print(name2.upper())
