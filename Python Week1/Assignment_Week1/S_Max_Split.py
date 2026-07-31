def solve():
    s = input()
    n = len(s)
    count_r = 0
    count_l = 0
    result = []
    current_string = ""
    for char in s:
        current_string += char
        if char == 'R':
            count_r += 1
        else:
            count_l += 1
        if count_r == count_l:
            result.append(current_string)
            current_string = ""
            count_r = 0
            count_l = 0
    
    print(len(result))
    for string in result:
        print(string)

solve()




