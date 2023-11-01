coin_types = [500, 100, 50, 10, 5, 1]  # 잔돈
price = int(input())  
count = 0

# 거스름돈
change = 1000 - price 
i = 0

while change != 0:

    # 거스름돈이 동전값보다 작으면 다음으로 작은 동전값 
    if change < coin_types[i]:
        i += 1

    count += change // coin_types[i]
    change %= coin_types[i]  

print(count)



