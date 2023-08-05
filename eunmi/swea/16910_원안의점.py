import sys
sys.stdin = open("input.txt")

# 테스트 케이스 정수로 받기
T = int(input())

for tc in range(1, T+1):
# 점 갯수 초기값 세팅
    N = int(input())
    count = 0
# 원안의 범위 지정 (양의 정수, 음의정수 포함)
    for i in range(-N, N+1):
        for j in range(-N, N+1):
# 정수 격자점 찾기
            if i**2 + j**2 <= N**2:
                count += 1
# 격자점 갯수 출력

    print(f'#{tc} {count}')