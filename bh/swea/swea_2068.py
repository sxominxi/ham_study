N =int(input())

for i in range(1,N+1):
    a = list(map(int,input().split()))
    #print('#{} {}'.format(i,max(a)))
    print(f'#{i} {max(a)}')