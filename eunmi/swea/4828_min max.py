T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # max와 min값을  arr의 0번째 인덱스로 세팅
    num_max = arr[0]
    num_min = arr[0]
    # max와 min값을 i랑 비교하면서 교체
    for i in arr:
        if num_max < i:
            num_max = i
        if num_min > i:
            num_min = i
    arr = num_max - num_min
    print(f'#{tc} {arr}')