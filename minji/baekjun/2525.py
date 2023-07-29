# 첫번째 줄 두 인자 받고
# 두번째 줄 인자 받기
time = list(map(int,input().split()))
time_1 = int(input())

# 받은 인자들 변수 할당
hour = time[0]
min = time[1]
given = time_1

# 함수 정의
def cook(H, M, T):
    M = M + T

    if (M + T) // 60 >= 1:
        M = M % 60
        H = H + (M // 60) # 왜 이게 안더해 지는거지 ㅠ ㅠ

        if H >= 24:
            H = H -24
        else:
            H = H + (M // 60)

    else:
        M = M + T
           
    print(f'{H} {M}')

# 함수에 맞게 변수 지정
cook(hour, min, given)

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