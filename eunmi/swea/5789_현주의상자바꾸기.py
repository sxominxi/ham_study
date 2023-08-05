# 테스트 케이스 정수로 받기
T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # [0]인덱스 상자 숫자만큼 만들기
    count = [0] * N
    # 변경하려는 횟수만큼 반복
    for i in range(1, Q+1):
    # 변경 범위
        L, R = map(int, input().split())
    # 변경 범위만큼 반복
        for j in range(L, R+1):
            count[j-1] = i

    print(f'#{tc}', end=" ")
    for i in range(len(count)):
        print(count[i], end=" ")
    print()