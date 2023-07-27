# 가장 첫 줄에는 테스트 케이스의 개수 T
T = int(input())

# 테스트 케이스 개수 T 만큼 주어지면 어떻게 나눠야 배분이 잘 될까 ?
for t in range(1, T + 1):
    test_case = list(map(int, input().split()))
    test_case.sort(reverse=True) # 얘가 문제네
    a = test_case[0]
    print(f'#{t} {a}')

i = 1

# 헉 이렇게 하니까 되네 왜지 ,,,
for test_case in range(1, T + 1):
    test_case = list(map(int, input().split()))
    print(f'#{i} {max(test_case)}')
    i += 1



