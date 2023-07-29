time = list(map(int,input().split()))
T = int(input())

hour = time[0]
min = time[1]
given = T[0]


def cook(H, M, T):
    M = M + T
    if M >= 60:
        H = H + 1
        M = M + 60 - 45
        if H > 24:
            H = 0

cook(hour, min, given)

# 왜 T가 활성화가 안되는 것임 !!!!
# 요리하는 데 필요한 시간 어캐 받아야 하는 것임 !!!!