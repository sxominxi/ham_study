N = int(input())
# 단수 입력 받기
for i in range(1,10): # 1~9단까지기 때문에 range 10
    print(N,"*",i,"=",(N*i)) # f-string 으로 표현해도 됨.