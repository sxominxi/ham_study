time = list(map(int,input().split()))

H = time[0]
M = time[1]

if M - 45 < 0:
    H = H - 1
    M = M + 60 - 45
    if H < 0:
        H = 23

elif M - 45 >= 0:
    M = M - 45

print(f'{H} {M}')



