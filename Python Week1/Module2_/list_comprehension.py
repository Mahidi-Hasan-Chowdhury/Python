numbers = [45,87,65,43,85,14,26,61]
odds=[]
for num in numbers:
    if num%2 ==1 and num%5==0:
        odds.append(num)

print(odds)

odd_nums = [num for num in numbers if num%2==1 if num%5==0]
print(odd_nums)

players = ['mahidi','siam','asif']
ages = [20,21,22]
player_age_comb = []
for player in players:
    print('player:',player)
    for age in ages:
        print(player,age)   
        player_age_comb.append([player,age])

print(player_age_comb)

age_comb2 = [[player,age] for player in players for age in ages]
print(age_comb2)