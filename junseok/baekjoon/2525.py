time = list(map(int,input().split()))
cook = int(input())

hour = time[0]
minute = time[1]

cook_h = hour + ( cook // 60 ) 
cook_m = minute + ( cook % 60 )

if cook_m >= 60:
    cook_m -= 60
    cook_h += 1

if cook_h >= 24:
    cook_h -= 24

print(f'{cook_h} {cook_m}')