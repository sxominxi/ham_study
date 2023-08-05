T = int(input())


for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] > 2:
                count += 1

    print(f'#{tc} {count}')