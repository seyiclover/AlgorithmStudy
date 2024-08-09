# top-down, 재귀, 메모이제이션

def DFS(len):
    
    # cut
    if dy[len] > 0: # 이미 값 구해져 있으면 그냥 씀
        return dy[len]
    
    # 메모이제이션
    if len==1 or len==2: # 1m(한 가지 방법) or 2m(두 가지)
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]


if __name__=="__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))
