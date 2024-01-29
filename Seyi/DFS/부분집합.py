def DFS(v):
    # 종료지점 출력
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    # 사용할지 안할지 여부 결정    
    else:
        ch[v]=1     # 사용하는 경우
        DFS(v+1)
        ch[v]=0     # 사용하지 않는 경우
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)