
# 테스트 케이스 정수로 받기
T = int(input())
# 테스트케이스만큼 반복
for tc in range(1, T+1):
    N = int(input())
    # [0]인덱스 소인수 리스트 숫자만큼 만들기
    count = [0] * 5
    # 소인수 리스트 만들기
    num = [2, 3, 5, 7, 11]
    a=0
    # 0번재 인덱스부터 나누기 시작해서 더이상 나눠지지 않을때까지 반복
    while a < 5:
        if N % num[a] == 0:
            N = N / num[a]
            count[a] += 1
        else:
            a += 1
    else:
        a = 0
        
    # 각각의 인덱스 count해서 출력
    print(f'#{tc}', end=" ")

    for i in range(5):
        print(count[i], end=" ")

    print()


