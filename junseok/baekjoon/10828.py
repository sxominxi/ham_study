import sys

N = int(input())

list1=[]
for i in range(1,N+1):
    order = list(map(str,sys.stdin.readline().split()))
    if order[0] == 'push':
        list1.append(order[1])

    elif order[0] == 'pop' :
        if len(list1) != 0:
            pop_num = list1.pop()
            print(pop_num)
        elif len(list1) == 0:
             print('-1')
    
    elif order[0] == 'size':
        print(len(list1))
        
    elif order[0] == 'empty' :
        if len(list1) == 0:
            print('1')
        else:
            print('0')
    elif order[0] == 'top':
        if len(list1) == 0:
            print('-1')
        else:
            print(list1[-1])
