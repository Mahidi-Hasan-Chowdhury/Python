def check(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")

check(12)              

look = lambda x: print("Even NUmber") if x %2 ==0 else print("Odd Number")
look(15)

addition = lambda a,b: a+b
print(addition(5,5))

total = lambda *args: sum(args)
print(total(1,2,3,4,5))