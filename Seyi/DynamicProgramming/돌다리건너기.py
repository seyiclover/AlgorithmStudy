# 돌다리를 건널 때 최소 보폭으로 도착까지 걸리는 걸음수는 n+1이다. 

n = int(input()) + 1
d = [0] * (n+1)
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    if d[i] == 0 :
        d[i] = d[i-1] + d[i-2]

print(d[n])
