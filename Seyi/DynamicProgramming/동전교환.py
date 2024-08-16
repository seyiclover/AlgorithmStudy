n = int(input())        # 동전의 종류 수
coins = list(map(int, input().split()))         # 동전의 종류 
m = int(input())        # 거스름돈 금액


dy=[float('inf')] * (m + 1)        # 해당 금액을 거슬러주는데 사용되는 동전의 최소 개수 저장    
dy[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        dy[i] = min(dy[i], dy[i - coin] + 1)

print(dy[m])
