N = int(input())

char = '*'
for i in range(1,N+1):
    print(f'{char.center(2*N-1)}')
    char += '**'

for i in range(N,2*N-1):
   