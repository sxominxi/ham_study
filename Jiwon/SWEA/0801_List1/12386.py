T = int(input())
K = 9
num = 0
for tc in range(1, T+1):
    N = int(input())
    a = list(map(str, input()))
    int_a = list(map(int, a))

    card = [0] * (K + 1)
    for i in int_a:
        card[i] = card[i] + 1
    idx = 0
    for j in range(K+1):
        if card[idx] <= card[j]:
            idx = j
    num += 1
    print(f'#{num} {idx} {card[idx]}')