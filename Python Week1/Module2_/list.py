#index =   0   1   2   3   4   5   6   7   8 
numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90]
#index =  -9   -8  -7  -6  -5  -4  -3  -2  -1 

print(numbers[3],numbers[-3])

#list (start:end)
print(numbers[2:6])

print(numbers[2:6:1])
print(numbers[2:6:2])
print(numbers[2:7:-1]) #none
print(numbers[7:2:-1])
print(numbers[7:2:-2])
print(numbers[7:2:2]) #none
print(numbers[4:]) #it will go to last
print(numbers[:5]) #it will start from first
print(numbers[:]) #it will go from 1st to last
print(numbers[::-1]) #it will reverse the list