T = int(input())
for ts in range(1, T+1):
    num = int(input())
    scores = list(map(int, input().split()))

    ans = [0] * 1000
    for j in scores:
        ans[j] += 1

    max_a = 0
    for num in range(1000):
        if ans[max_a] <= ans[num]:
            max_a = num
    print(f'#{ts} {max_a}')