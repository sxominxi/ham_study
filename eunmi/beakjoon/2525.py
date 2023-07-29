import sys


# 1
# 잘못된 코드 b+c가 2시간이상 초과 될 경우를 생각하지 못함
A, B = map(int, sys.stdin.readline().split())
C = int(input())

if  B + C > 60:
    B = (B + C) -60
    A = A + 1
    print(A, B)
   
elif A == 23 and B + C > 60:
    a = 0
    B = (B + C)-60
    print(a, B)
elif B + C == 60:
    A = A + 1
    b = 0
    print(A, b)
elif B + C < 60:
    B = B + C
    print(A, B)

# 2
A, B = map(int, sys.stdin.readline().split())
C = int(input())

# B + C >= 60 일경우, 시간은 60으로 나눈 몫으로 분은 나머지로 받기
hour = (B + C) // 60
min = (B + C) % 60

# hour이 24시 이상일 경우와 아닐경우로 나누기
if B + C >= 60:
    if A + hour >= 24:
        A = A -24
    A = A + hour
    print(A, min)

# B+c가 60 미만일 경우에는 hour 경우의 수 생각하지 않기
else:
    if B + C < 60:
        print(A, B+C)