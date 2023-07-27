N = int(input())
sum = 0
a=0
 
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in data:
            if int(j) % 2 != 0:
                sum += int(j)
 
            else :
                continue
         
    print("#"+str(i),sum)
    sum = 0