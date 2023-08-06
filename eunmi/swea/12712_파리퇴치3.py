import sys
sys.stdin = open('input.txt')

# 테스트 케이스 정수로 받기
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
# 한줄씩 리스트로 받기
    arr = [list(map(int, input().split())) for _ in range(N)]
# 1. 상하좌우 분사
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
# 2. 대각선 분사
    ci = [-1, -1, 1, 1]
    cj = [-1, 1, -1, 1]

# 최댓값 초기값 세팅
    kills = 0
# 행 열 N*N 만큼 반복
    for i in range(N):
        for j in range(N):
# 상하좌우 좌표 세팅
            s1 = arr[i][j]
# 대각선 좌표 세팅
            s2 = arr[i][j]

# 검색용 배열 내 모든 방향 반복
            for k in range(4):
# M의 세기로 분사
                for l in range(1, M):
                    r1, r2 = i + di[k]*l, j + dj[k]*l
                    c1, c2 = i + ci[k]*l, j + cj[k]*l

                    # 배열안에 들어있는지 확인
                    if 0 <= r1 < N and 0 <= r2 < N:
                    # 상하좌우 좌표 담기
                        s1 += arr[r1][r2]
                    if 0 <= c1 < N and 0 <= c2 < N:
                    # 대각선 좌표 담기
                        s2 += arr[c1][c2]
        # 최댓값 구하기
            if s1 > kills:
                kills = s1
            if s2 > kills:
                kills = s2
    
    print(f'#{tc} {kills}')