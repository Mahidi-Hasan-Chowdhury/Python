def max_operations(n, a):
    operations = 0

    while True:
        # Check if all numbers are even
        if all(x % 2 == 0 for x in a):
            # Divide all numbers by 2
            a = [x // 2 for x in a]
            operations += 1
        else:
            break
    
    return operations

# Input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(max_operations(n, a))
