dice = list(map(int,input().split()))

dice1 = dice[0]
dice2 = dice[1]
dice3 = dice[2]
reward = 0

if dice1 == dice2 == dice3:
    reward = 10000 + 1000*dice1

elif dice1 == dice2: 
    reward = 1000 + 100*dice1
elif dice1 == dice3:
    reward = 1000 + 100*dice1
elif dice2 == dice3:
    reward = 1000 + 100*dice2

else:
    reward = max(dice)*100

print(reward)
