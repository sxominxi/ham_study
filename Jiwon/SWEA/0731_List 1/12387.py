T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    max_val = 0
    min_val = 1e10
    for i in range(N-M+1):
        val = 0
        for j in range(M):
            val = val + ai[i + j]

        if max_val < val:
            max_val = val

        if min_val > val:
            min_val = val

    print(f'#{tc} {max_val - min_val}')