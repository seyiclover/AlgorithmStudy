# 전위순회
def DFS(v):
    # 7까지만 조회
    if v>7:
        return 
    else:
        print(v)    # 전위순회
        DFS(v*2)    # 왼쪽노드 
        DFS(v*2+1)  # 오른쪽노드

if __name__=="__main__":
    DFS(1)

# 중위순회
def DFS(v):
    # 7까지만 조회
    if v>7:
        return 
    else:
        DFS(v*2)    # 왼쪽노드 
        print(v)    # 중위순회
        DFS(v*2+1)  # 오른쪽노드

if __name__=="__main__":
    DFS(1)

# 후위순회
def DFS(v):
    # 7까지만 조회
    if v>7:
        return 
    else:
        DFS(v*2)    # 왼쪽노드 
        DFS(v*2+1)  # 오른쪽노드
        print(v)    # 후위순회

if __name__=="__main__":
    DFS(1)
