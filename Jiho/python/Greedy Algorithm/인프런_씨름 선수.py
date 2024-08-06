n = int(input())

players = []
for i in range(n):
    h, w = map(int, input().split())
    players.append((h, w))

players.sort(reverse=True)
check_w = 0
cnt += 0

for h, w in players:
    if w > check_w:
        cnt += 1
        check_w = w

print(cnt)
