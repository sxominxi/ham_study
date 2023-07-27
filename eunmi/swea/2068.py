T = int(input())
for test in range(1, T+1):
    num_list = list(map(int, input().split()))
    num_max = max(num_list)
    print(f'#{test} {num_max}')

# max를 사용하지 못할 경우
T = int(input())
for test in range(1, T+1):
    res = 0
    num_list = list(map(int, input().split()))
    for x in num_list:
        if x >= res:
            res = x
    print(f'#{test} {res}')