N = int(input())
a = list(map(int, input().split()))
a.sort()
a_index = int(N/2)
print(a[a_index])