T = 10

for tc in range(1, T+1):
    num = int(input())
    dump = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    for j in range(num):
        for i in range(len(dump)):
            if dump[max_idx] < dump[i]:
                max_idx = i

            if dump[min_idx] > dump[i]:
                min_idx = i

        dump[max_idx] = dump[max_idx] - 1
        dump[min_idx] = dump[min_idx] + 1

        for i in range(len(dump)):
            if dump[max_idx] < dump[i]:
                max_idx = i

            if dump[min_idx] > dump[i]:
                min_idx = i

    ans = dump[max_idx] - dump[min_idx]

    print(f'#{tc} {ans}')