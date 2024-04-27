card = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        card[a+i-1], card[b-i-1] = card[b-i-1], card[a+i-1]

for x in card:
    print(x, end=' ')
