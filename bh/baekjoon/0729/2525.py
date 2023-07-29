h,m=map(int, input().split())
t =int(input())
# 시간과 분을 먼저 입력하고 요리 시간을 입력
if m+t >=60: # 60분이 초과될 경우 시간으로 변환하여 더해주고
             # 남은 시간을 다시 분에 입력
    h += (m+t)//60
    m =(m+t)%60
    if h>=24: # 시간이 24시가 초과 될 경우 다시 0시가 되기 때문에 이를 변환
        print(h-24,m)
    else:
        print(h,m)
else:
    print(h,m+t)