# A+B - 3
# T 줄만큼 A + B 구하기

T = int(input())


for i in range(1, T+1):
    A, B = map(int,input().split())
    print(A + B)