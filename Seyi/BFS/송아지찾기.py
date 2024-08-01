from collections import deque
MAX = 10000        # 좌표의 최댓값
ch = [0] * (MAX+1)  # 방문여부 체크 
dis = [0] * (MAX+1) # 최소 이동 횟수 기록

n, m = map(int, input().split())    # n: 출발점, m: 도착점
ch[n] = 1           # 출발점 방문 체크 
dis[n] = 0          
dQ = deque()
dQ.append(n)

while dQ:           # dequeq가 빌 때까지 반복
    now=dQ.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5):   # 이동: +1, -1, +5
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[m])
