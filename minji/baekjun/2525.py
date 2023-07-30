import sys

# 첫번째 줄 두 인자 받고
# 두번째 줄 인자 받기
time = list(map(int, sys.stdin.readline().split()))
time_1 = int(sys.stdin.readline())

hour = time[0]
min = time[1]
given = time_1

if (min + given) // 60 >= 1:
    hour = hour + ((min + given) // 60)
    min = (min + given) % 60

    if hour >= 24:
        hour -= 24
        print(f'{hour} {min}')
    else:
        print(f'{hour} {min}')

else:
    min += given
    print(f'{hour} {min}')

# 함수 때문인지 런타임 에러 발생

# # 받은 인자들 변수 할당
# hour = time[0]
# min = time[1]
# given = time_1

# # 함수 정의
# def cook(H, M, T):
#     M = M + T

#     if (M + T) // 60 >= 1:
#         minute = M % 60
#         hour1 = H + (M // 60) # 왜 이게 안더해 지는거지 ㅠ ㅠ > 해결 !

#         if hour1 >= 24:
#             hour1 -= 24
#             print(f'{hour1} {minute}')
#         else:
#             hour1 = H + (M // 60)
#             print(f'{hour1} {minute}')
            

#     else:
#         minute = M + T
#         print(f'{hour1} {minute}')

# # 함수에 맞게 변수 지정
# cook(hour, min, given)

# 왜 T가 활성화가 안되는 것임 !!!!
# 요리하는 데 필요한 시간 어캐 받아야 하는 것임 !!!!
# time = list(map(int,input().split()))
# T = int(input())

# hour = time[0]
# min = time[1]
# given = T[0]


# def cook(H, M, T):
#     M = M + T
#     if M >= 60:
#         H = H + 1
#         M = M + 60 - 45
#         if H > 24:
#             H = 0

# cook(hour, min, given)