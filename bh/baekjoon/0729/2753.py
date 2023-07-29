year =int(input())
# 원하는 년도를 입력
if year % 400 == 0: # 400의 배수일 때
    print('1')
elif year % 4 ==0 and year % 100 != 0: # 4의 배수이면서 100의 배수가 아닐때
    print('1')
else: #이외에는 모두 윤년이 아님
    print('0')
    