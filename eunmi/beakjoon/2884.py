H, M = map(int, input().split())

if (45<= M <= 60):
    m = M-45
    print(H, m)
elif H == 0 and (0 <= M <= 44):
    H = 23
    m = 60-45+M
    print(H, m)
elif 1 <= H <= 23 and (0 <= M <= 44):
    h = H-1
    m = 60-45+M
    print(h, m)