import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    numbers = []
    # 구간설정
    for i in range(N-M+1):
    # i부터 i+M까지 더한 값을 count에 저장
        new_num = arr[i:i+M]
        count = 0
        for i in new_num:
            count += i
        numbers.append(count)
    print(numbers)

    # 가장 큰값과 작은값으로 세팅
    mini = 10e9
    maxi = 0

    for i in numbers:
        if mini > i:
            mini = i
    for i in numbers:
        if maxi < i:
            maxi = i

    print(f'#{tc}', maxi - mini)