# 오븐 시계
# 요리하는데 필요한 시간을 계산해 요리 끝나는 시간을 출력

A, B = map(int, input().split())
M = int(input())

# 걸리는 시간 = 현재 분 + 필요한 시간
take_long = B + M  

# 걸리는 시간이 60분이 넘었을 때
if take_long >= 60:
    # 60분으로 나눈 몫만큼 현재 시에 더해줌
    hour = A + take_long // 60
    # 60분으로 나눈 나머지만큼 현재 분에 더해줌
    minute = take_long % 60

    # 시가 24시가 넘으면 24시를 빼줌
    if hour >= 24:
        hour = hour - 24
    print(hour, minute)
    
else:
    print(A, take_long)