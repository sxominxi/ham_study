N = int(input())
max_F = 0
 
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in data:
            max_F = max(data)
         
    print("#"+str(i),max_F)
    max_F = 0