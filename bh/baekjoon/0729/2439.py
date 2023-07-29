n = int(input())
for i in range(n):
    s ='*'
    b =' ' 
    print(b*(n-(i+1))+s*(i+1))
    # 별 개수가 공백 개수를 변경하는 코드.
    # 횟수가 증가할수록 공백은 줄어들고, 별은 늘어난다.