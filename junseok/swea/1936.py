data = list(map(int, input().split()))

if data[0] == data[1]+1 :
    print('A')
elif data[0]==1 and data[1]==3:
    print('A')

elif data[0] == data[1]-1 :
    print('B')

elif data[0]==3 and data[1]==1:
    print('B')