def solve():
    n = int(input())
    a = list(map(int, input().split()))

    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    removed = 0

    for num, count in freq.items():
        if count == num:
            continue
        elif count > num:
            removed += count - num
        else:
            removed += count
            
    print(removed)

solve()



# USing counter solve

# from collections import Counter

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     # Count the frequency of each number
#     freq = Counter(a)
#     removed = 0

#     # Iterate over the frequency dictionary
#     for num, count in freq.items():
#         if count == num:
#             continue
#         elif count > num:
#             removed += count - num
#         else:
#             removed += count
            
#     print(removed)

# solve()
