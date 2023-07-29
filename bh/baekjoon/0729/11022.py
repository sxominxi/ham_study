t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(i+1,a,b,a+b)) # 이제 f-string을 사용하자