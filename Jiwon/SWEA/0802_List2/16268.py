T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[]for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    arr_max = 0
    # 1. find
    for r in range(N):
        for c in range(M):
            com_arr = 0
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            com_arr = arr[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    com_arr += arr[nr][nc]

                # 2. compare
                if arr_max < com_arr:
                    arr_max = com_arr
    print(f'#{tc} {arr_max}')