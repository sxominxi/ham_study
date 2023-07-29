# 알람 시계
# 45분 이전으로 되돌려 놓기

H, M = map(int, input().split())

# 0시 이고 45분 이전일 때
if H == 0 and 0 <= M < 45:  
    minute = M + 15         # 분은 15분 더해지고
    hour = 23               # 시간은 23시가 됨.

# 0시보다 크고 45분 이전일 때
elif H > 0 and 0 <= M < 45: 
    minute = M + 15         # 분은 15분 더해지고
    hour = H - 1            # 시간은 1시간씩 빠짐.

# 45분 이전일 때
elif 45 <= M <= 59:   
    minute = M - 45         # 45분 이전으로 되돌리고
    hour = H                # 시간은 영향을 받지 않음.

print(hour, minute)