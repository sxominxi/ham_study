import sys
sys.stdin = open('input_11151.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    new_num = []
    max_n = 0
    for i in range(N-1):
        new_num.append(num[i] + num[i+1])
    for j in new_num:
        if max_n < j:
            max_n = j
    print(f'#{tc} {max_n}')


