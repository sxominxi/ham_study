# 주사위 세개

a, b, c = map(int, input().split())

# 다 같은 눈인 경우
if a == b == c:
    print(10000 + a * 1000)

# 셋 중 두 개만 같은 눈인 경우
elif a == b != c or a == c != b:
    print(1000 + a * 100)

elif a != b == c:
    print(1000 + b * 100)

# 다 다른 눈인 경우
elif a != b != c:
    print(max(a, b, c) * 100)