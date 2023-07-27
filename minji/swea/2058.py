# 자연수 N 입력
N = input() 
# print(type(N)) = <class 'str'>

# 얘를 뭐라고 할까
i = 0

# N에 있는 숫자 num을 하나하나 실행
for num in N:
    i += int(num)
print(i)

# list, sum 함수 사용
