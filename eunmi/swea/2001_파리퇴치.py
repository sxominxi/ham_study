import sys
sys.stdin = open("input.txt")

# 1
# 테스트 케이스 정수로 받기
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# 잡은 파리의 수를 담을 리스트 생성
    kill_bug = []
# 파리채를 내려칠 범위 탐색
    for i in range(N-M+1):
        for j in range(N-M+1):
# 파리의 수 초기값 세팅
            kills = 0
# 잡을 수 있는 파리의 수 탐색
            for k in range(M):
                for l in range(M):
                    kills += arr[i+k][j+l]
# 리스트에 담기
            kill_bug.append(kills)
# 가장 많이 잡은 파리의 수 출력
    print(f'#{tc}', max(kill_bug))



# 2
# 테스트 케이스 정수로 받기
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# 잡은 파리의 수를 담기위해 초기값 세팅
    kill_bug = 0
# 파리채를 내려칠 범위 탐색
    for i in range(N-M+1):
        for j in range(N-M+1):
# 파리의 수 초기값 세팅
            kills = 0
# 잡을 수 있는 파리의 수 탐색
            for k in range(M):
                for l in range(M):
                    kills += arr[i+k][j+l]
# 리스트로 append하지않고 max안쓰고 찾는 방법
                if kills > kill_bug:
                    kills = kill_bug
    print(f'#{tc} {kills}')