# 맵 크기 입력
n = int(input())    
# 이동 계획 입력
plans = list(map(str, input().split()))     
x, y = 1, 1     # 시작 위치

# L, R, U, D 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동 계획에 따라 이동
for plan in plans:
    if plan == 'L':
        nx = x + dx[0]
        ny = y + dy[0]
    elif plan == 'R':
        nx = x + dx[1]
        ny = y + dy[1]
    elif plan == 'U':
        nx = x + dx[2]
        ny = y + dy[2]
    elif plan == 'D':
        nx = x + dx[3]
        ny = y + dy[3]
    # 맵을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
