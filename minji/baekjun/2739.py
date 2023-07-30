# 입력값 N 받기
N = int(input())


i = 1   # i는 1 부터 시작
while i <= 9:   # i가 9일 때 동안 실행
    gugudan = N * i
    print(f'{N} * {i} = {gugudan}')
    i += 1  # i 카운트

# while은 종료 조건을 내가 설정해줘야된다.