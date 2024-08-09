# 이진트리 순회 DFS

# 전위 순회
def DFS(v): # node
    if v > 7:
        return
    else:
        print(v, end=" ") # root
        DFS(v*2) # 왼쪽 자식 node
        DFS(v*2+1) # 오른쪽 자식 node

# 중위 순회
def DFS(v): 
    if v > 7:
        return
    else:
        DFS(v*2) # 왼쪽 자식 node
        print(v, end=" ") # root
        DFS(v*2+1) # 오른쪽 자식 node

# 후위 순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2) # 왼쪽 자식 node
        DFS(v*2+1) # 오른쪽 자식 node
        print(v, end=" ") # root
