a=20
print("even number") if a%2==0 else print("odd number") # Ternary operator in Python to check if a number is even or odd

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

b=[]

for i in a:
    if i%2==0:
        b.append(i)

print(b) 

c = [i for i in a if i%2==1]
print(c)
