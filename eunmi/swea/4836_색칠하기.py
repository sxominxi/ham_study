# 테스트 케이스 정수로 받기
T = int(input())

# for문 전체 테스트 케이스만큼 반복
for tc in range(1, T+1):
# n정수로 받기
    N = int(input())
# arr리스트에 정수로 받고 10*10만큼 인덱스만들고 0으로 세팅
    arr = [[0]* 10 for _ in range(10)]
# 겹쳐진 보라색 케이스 = 0 세팅
    purple = 0

# for문 n번만큼 반복
    for i in range(N):
# r1, c1, r2, c2, color 정수로 받기
        r1, c1, r2, c2, color = map(int, input().split())
        # for문 i행 range (r1, r2+1)
        for i in range(r1, r2+1):
        # for문 j열 range (c1, c2+1)
            for j in range(c1, c2+1):
                arr[i][j] += color
# 칠해진 숫자가 3일때,
                if arr[i][j] == 3:
                    purple += 1
    print(f'#{tc} {purple}')

