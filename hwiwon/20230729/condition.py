### 1330
A, B = map(int, input().split())

if A > B:
    print('>')
elif A == B:
    print('==')
elif A < B:
    print('<')



###9498
A = int(input())  

if 90 <= A <= 100:
    print('A')
elif 80 <= A <= 89:
    print('B')
elif 70 <= A <= 79:
    print('C')
elif 60 <= A <= 69:
    print('D')
else:
    print('F')

###2753
year = int(input())

if year % 4 == 0:
    if year % 400 == 0:
        print('1')
    elif year % 100 == 0:
        print('0')
    else:
        print('1')
else: 
    print('0')

### 14681
x = int(input())
y = int(input())

if (0 < x) and (0 < y):
    print (1)
if (0 > x) and (0 < y):
    print (2)
if (0 > x) and (0 > y):
    print (3)
if (0 < x) and (0 > y):
    print (4)


### 2884

H, M = map(int, input().split())

if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60

print(H, M - 45)


### 2525
A, B = map(int, input().split())
C = int(input())

Hrs = (C + B) // 60

if Hrs == 0:
    B += C
elif Hrs >= 1:
    A += Hrs
    B = (C + B) % 60
    if A >= 24:
        A = A - 24

# B + C 값은 분을 더했을 때.
# B+C//60 -> 몫이 0이라면 분만 B 값에 C 만 더하기
# 몫이 0 이상일 땐 시간에 몫을 더하고 b 는 B+C 값을 60으로 나눈 나머지값이 됨
# A 값이 24 이상이 되면 다시 0부터 시작해야 하기 때문에 최종 A 값 - 24를 하면 됨    

print(A, B)


### 2480
A, B, C = map(int, input().split())

if (A == B) and (B == C):
    print(10000 + A * 1000)
elif (A == B) or (A == C):
    print (1000 + A * 100)
elif (B == C):
    print (1000 + B * 100)
else:
    print(max(A, B, C) * 100)