from collections import deque

def bfs_maze(maze):
    # 미로의 크기
    n = len(maze)
    m = len(maze[0])
    
    # 상, 하, 좌, 우 이동을 위한 좌표 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐 생성
    queue = deque([(0, 0)])  # 시작점 (0, 0)부터 탐색 시작
    
    while queue:
        x, y = queue.popleft()  # 현재 위치
        
        # 상하좌우로 이동할 수 있는 곳을 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽인 경우 무시
            if maze[nx][ny] == 0:
                continue
            
            # 처음 방문하는 곳일 경우, 해당 위치까지의 거리를 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    # 출구까지의 최단 경로 반환
    return maze[n-1][m-1]

maze1 = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

maze2 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# 최단 경로 출력
print(bfs_maze(maze1))  # 8
print(bfs_maze(maze2))  # 9
