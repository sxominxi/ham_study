x =int(input())
y =int(input())
# x,y 좌표를 입력하고,
if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
else:
    print('4')
   # 1사분면은 x,y 모두 양수
   # 2사분면은 x 음수, y 양수
   # 3사분면은 x,y 모두 음수
   # 4사분면은 x 양수, y 음수 
   # 각각의 조건을 if elif 문에 구성