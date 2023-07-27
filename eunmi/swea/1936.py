A, B = map(int, input().split())
# rock = 2
# scissors = 1
# paper = 3
if A == 1 and B == 3:
    print('A')
elif A ==3 and B == 1:
    print('B')
elif A>B:
    print('A')
elif A<B:
    print('B')