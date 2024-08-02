from collections import deque

dx = [-1, 0, 1, 0]      # 12시, 3시, 6시, 9시 방향 이동 
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ch = [[0] * n for _ in range(n)]    # 방문여부 체크
sum = 0     # 총합
Q = deque()

ch[n // 2][n // 2] = 1     # 정중앙 방문 체크
sum += a[n//2][n//2]       # 정중앙 값 sum 에 추가
Q.append((n//2, n//2))
L = 0                      # 현재 레벨

while True:
    if L == n // 2:        # 종착점
        break
    size = len(Q)          # 레벨의 노드의 개수 
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):  # 4방향 이동 
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1

print(sum)
