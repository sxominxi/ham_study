import sys # 빠른 출력을 위해 sys를 import한다.
input = sys.stdin.readline # 빠른 출력을 위한 명령어
t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(a+b)
    #이를 적용하지 않으면 이 문제에서는 오류가 발생한다.