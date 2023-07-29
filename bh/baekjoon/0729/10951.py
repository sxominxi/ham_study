while True:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break

# EOF(End Of File) 에러를 해결하기 위한 try, except 문.
# 입력이 끝날 때 종료하게끔 코드를 구성할 수 있다.