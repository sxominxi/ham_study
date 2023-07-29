time = list(map(int,input().split()))

hour = time[0]
minute = time[1]

if minute - 45 < 0:
    minute += 60 - 45
    hour -= 1
    if hour < 0 :
        hour = 23
else:
    minute -= 45
    

print(f'{hour} {minute}')