import sys
sys.stdin = open('input_2001.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = []
    dc = []
    for r in range(M):
        if r == 0:
            dr.append([0] * (M-1))
        else:
            dr.append([r] * M)
        for c in range(M):
            dc.append([c] * M)
    print(dr)
    print(dc)


