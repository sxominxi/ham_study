# 가장 첫 줄에는 테스트 케이스의 개수 T
T = int(input())

# 테스트 케이스 개수 T 만큼 주어지면 어떻게 나눠야 배분이 잘 될까 ?
# test_case = list(map(int, input().split()))

# 헉 이렇게 하니까 되네 왜지 ,,,
for test_case in range(1, T + 1):
    test_case = list(map(int, input().split()))

# 얘는 list
# print(type(test_case))

for num in test_case:
    test_case.sort(reverse=True) # 얘가 문제네
    a = test_case[0]

i = 1

while i <= T:
    print(f'#{i} {a}')
    i += 1

# 왜 안됨 !!!!!!!!!!! 
# 마지막 리스트 것만 출력되잔아 ㅠ ㅠ ㅠ ㅠ ㅠ



