n = 7
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2

def DFS(n):
    if n == 1 or n == 2:
        return n
    
    # 메모이제이션
    if dy[n] > 0:
        return dy[n]
    
    else:
        dy[n] = DFS(n-1) + DFS(n-2)
        return dy[n]

print(DFS(n))
