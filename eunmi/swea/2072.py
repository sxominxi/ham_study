T = int(input())
for test in range(1, T+1):
    num_list = map(int, input().split())
    res = []  # 결과값을 저장한 빈 리스트가 필요
    for i in num_list:
        if i % 2 != 0:
            res.append(i)
    print(f'#{test} {sum(res)}') # sum을 print에서 할 것