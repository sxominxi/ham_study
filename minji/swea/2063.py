# 첫 줄에 N 입력
N = int(input())

# input 된 숫자들 띄어쓰기로 나눠서 입력 / map 함수로 다 int / 그런데 list인
data = list(map(int, input().split()))

# data 정렬
data.sort()

# 그 중에서 딱 절반값 프린트 근데 왜 대괄호지 ?
print(data[N//2])