import sys
sys.stdin = open('input_12383.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    blocks = list(map(int, input().split()))
    com = []                             #
    for i in range(N-1):                 # N-2 인덱스까지 순회
        cnt = 0
        for j in range(i+1, N):          # blocks[i]와 i뒤에 있는 요소들을 다 비교
            if blocks[i] <= blocks[j]:   # 만약 뒤에 있는 것들 중 더 큰게 있다면
                cnt += 1                 # 큰거 몇 개 있는지 세기
        ans = N - (i+1) - cnt            # 얼마나 낙하하는지 = 총 갯수 - 내가 있는 위치 - 나보다 큰 블록의 수
        com.append(ans)                  # 낙차 수를 비교하기 위해 com에 더함

    max_i = 0
    for i in com:                       # com에 있는 낙차 수 중 가장 큰 것을 비교
        if max_i < i:
            max_i = i
    print(f'#{tc} {max_i}')



