score =int(input()) # 성적을 입력 받고
if 90<=score<=100: #if 와 elif를 사용하여 조건에 맞는 부분 출력
    print('A')
elif 80<=score<90:
    print('B')
elif 70<=score<80:
    print('C')
elif 60<=score<70:
    print('D')
else:
    print('F')