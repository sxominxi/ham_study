import sys

N = int(input())

set1= set()
for i in range(1,N+1):
    set1.add(int(sys.stdin.readline()))


for j in list(sorted(set1)):
    print(j)