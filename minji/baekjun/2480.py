dice = list(map(int, input().split()))

a = dice[0]
b = dice[1]
c = dice[2]

prize = 0

if a == b and b == c:
    prize = 10000 + a * 1000

elif a == b:
    prize  = 1000 + a * 100

elif a == c:
    prize  = 1000 + a * 100

elif c == b:
    prize  = 1000 + c * 100

else:
    prize = max(dice) * 100
    # for i in dice:
    #     list_dice = dice.sort()
    #     i = list_dice[0]

print(prize)
        
# 의문 : if로 했을 때랑 elif로 했을 때랑 값이 다르던데 왜지