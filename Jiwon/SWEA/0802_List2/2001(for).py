import sys
sys.stdin = open('input_2001.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]      # N X N 행렬 생성

    com = []                           # 케이스 바뀔 때 마다 큰 값을 비교하는 리스트 초기화
    for r in range(N-M+1):             # 파리채의 (0,0)이 갈 수 있는 최대 인덱스 = N-M
        for c in range(N-M+1):         # 하나의 행에 있는 열 다 돌고
            kill_fly = 0               # 파리채 한 번 하고 초기화
            for nr in range(M):        # 파리채 크기안에서 파리 한 칸씩 잡기
                for nc in range(M):
                    kill_fly += arr[r+nr][c+nc]  # r, c가 기준점정해주는거 + nr, nc가 파리채 안에서 파리 잡기
            com.append(kill_fly)       # 파리채 한 번에 잡은만큼 털기

    max_k = 0             # 어디가 많이 잡았나 비교
    for m in com:
        if max_k < m:
            max_k = m
    print(f'#{tc} {max_k}')
