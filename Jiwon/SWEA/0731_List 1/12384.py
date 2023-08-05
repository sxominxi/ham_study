T = int(input())

for tc in range(1, T+1):

    N =int(input())
    arr = list(map(int, input().split()))
    max_val = min_val = arr[0]
    for val in arr:
        if max_val <= val:
            max_val = val
        if min_val >= val:
            min_val = val
    ans = max_val - min_val

    print(f'#{tc} {ans}')