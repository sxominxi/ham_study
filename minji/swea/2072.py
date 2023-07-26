# 테스트 케이스의 개수 T
T = int(input())

# 테스트 케이스 정보 받기 ?
for i in range(1, T + 1):
    a = list(map(int, input().split()))

# print(a)는 
# [3, 17, 1, 39, 8, 41, 2, 32, 99, 2]
# [22, 8, 5, 123, 7, 2, 63, 7, 3, 46]
# [6, 63, 2, 3, 58, 76, 21, 33, 8, 1]

# 리스트 안에 있는 num 중 홀수만 빼서 리스트 만들기
    for num in a:
        if num % 2 == 1:
            b = [num]

    print(b)

n = 0
for nums in b:
    n += num

print(f'#{i} {n}')

