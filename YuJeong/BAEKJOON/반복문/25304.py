# 영수증

# 영수증에 적힌 총 금액 X
X = int(input())

# 영수증에 적힌 물건 종류의 수 N
N = int(input())

price = 0
for _ in range(N):
    # 각 물건의 가격 a와 개수 b
    a, b = map(int,input().split())
    price = price + (a * b)  # 영수증에 적힌 물건의 가격을 모두 더한 총액

if price == X:  # 총액이 영수증에 적힌 총액과 같다면
    print('Yes')   # yes 출력

else:
    print('No')