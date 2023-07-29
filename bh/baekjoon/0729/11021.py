t = int(input()) # 값을 입력받고
for i in range(t):
    a,b = map(int, input().split()) # 두 개 값을 동시 입력 받기 위한 map 함수
    print('Case #{}: {}'.format(i+1,a+b)) # f-string 이전의 구형 구현