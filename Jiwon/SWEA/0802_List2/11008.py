import sys
sys.stdin = open('input_11008.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, (input().split()))) for _ in range(N)]

    dr = [0, 1, 0, -1]      # 상하좌우 델타값 리스트
    dc = [1, 0, -1, 0]

    r_num = []              # 최댓값일때의 r, c값을 알기위해 각각의 r,c 값을 매번 저장 할 공간 생성
    c_num = []
    com = []
    for r in range(N):      # 행 순회
        for c in range(N):  # 열 순회
            sum_arr = 0     # 델타 한 세트 돌린 후 sum 초기화
            for k in range(4):
                nr = r + dr[k]  # 기준점위치 + 델타값 = 상하죄우
                nc = c + dc[k]
                if 0 <= nc < N and 0 <= nr < N:  # 상하좌우 인덱스가 기존 행렬을 넘어가지 않는 것만
                    sum_arr += arr[nr][nc]       # sum 값에 더함
            com.append(sum_arr)
            r_num.append(r)        # 한 세트의 기준점의 r, c값 추가
            c_num.append(c)
    ans = 0
    for i in range(N*N):    # N * N == len(com)
        if ans < com[i]:    # 크기 비교
            ans = com[i]
            ar = r_num[i]   # 클 때마다 그때의 r,c값 찾기
            ac = c_num[i]
    print(f'#{tc} {ar} {ac} {ans}')

