T = int(input())    # test case 받기

for i in range(1, T + 1):   # for 문
    A, B = map(int, input().split())
    print(A + B)

# for 문은 조건에 맞게 종료 조건 실행
# 알아서 i 카운트