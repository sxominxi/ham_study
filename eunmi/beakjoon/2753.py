year = int(input())

# 4의 배수이면서 100의 배수가 아닐때, => 두가지다 만족
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(1)
else:
    print(0)