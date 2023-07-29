numbers = list(map(int,input().split()))

if numbers[0] > numbers[1]:
    print('>')
elif numbers[0] == numbers[1]:
    print('==')
elif numbers[0] < numbers[1]:
    print('<')