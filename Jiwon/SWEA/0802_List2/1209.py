import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    compare = []
    arr = [[]for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    # 1. row sum

    row_max = 0
    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += arr[r][c]
        if row_max < row_sum:
            row_max = row_sum
    compare.append(row_max)

    # 2. col sum
    col_max = 0
    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += arr[r][c]
        if col_max < col_sum:
            col_max = col_sum
    compare.append(col_max)

    # 3. cross line
    # 3-1.
    cross_sum = 0
    # for r, c in range(100):
    for rc in range(100):
        cross_sum += arr[rc][rc]
    compare.append(cross_sum)

    # 3-2.
    cross_sum2 = 0
    for r in range(100):
        cross_sum2 += arr[r][100-1-r]
    compare.append(cross_sum2)

    # 4. compare
    ans = 0
    for i in compare:
        if ans < i:
            ans = i

    print(f'#{tc} {ans}')
