# A, B 받기
A, B = map(int, input().split())

# 조건문
if A > B:
    print(">")

elif A < B:
    print("<")

elif A == B:
    print("==")

# 의문 : range(-10000, 10001)는 안되던데 제한은 내가 두는게 아니라 그냥 입력값 말하는건가 ?