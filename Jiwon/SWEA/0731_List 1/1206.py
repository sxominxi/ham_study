for tc in range(1, 11):
    N = int(input())
    h = list(map(int, input().split()))

    # num.i sight
    # h[i]
    ans = 0
    for i in range(2, N-2):
        # maxh = max(h[i-2], h[i-1], h[i+1], h[i+2])
        maxh = h[i-2]
        if maxh < h[i-1]: maxh = h[i-1]
        if maxh < h[i+1]: maxh = h[i+1]
        if maxh < h[i+2]: maxh = h[i+2]


        if h[i] > maxh:
            ans += h[i] - maxh
    print(f'#{tc} {ans}')