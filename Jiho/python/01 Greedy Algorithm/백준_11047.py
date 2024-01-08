import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for i in range(N): 
    coins.append(int(sys.stdin.readline()))

coins = sorted(coins, reverse=True)

cnt = 0
rest = K

for coin in coins:
    while rest >= coin:
        cnt += (rest//coin)
        rest %= coin
    

print(cnt)
