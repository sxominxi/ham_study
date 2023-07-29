while True: # 루프를 이용하여 특정 조건 전까지는 계속 반복하도록 작성
    a,b = map(int,input().split())
    if a==b==0: # a와 b가 모두 0일때만 탈출(맨 마지막에 0이 오기 때문에)
        break
    else:   
        print(a+b)