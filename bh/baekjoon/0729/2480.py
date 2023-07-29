a,b,c=map(int, input().split())
# 주사위 세개
if a==b==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
elif c==a:
    print(1000+c*100)
else:
    print(max(a,b,c)*100)
# if 문을 어떻게 사용하느냐에 따라 개수를 줄일 수도 있을
# 것 같음. 