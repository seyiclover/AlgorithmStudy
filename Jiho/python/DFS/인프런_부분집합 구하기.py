def DFS(v): # 노드: 원소 값
    if v == n+1: # n까지가 원소임
        for i in range(1, n+1):   # 종료지점: 값 1인 index(사용하는 원소) 출력
            if ch[i]==1:
                print(i, end=' ')
            print()

    else:           # 원소 사용여부 결정
        ch[v]=1         # 1이면 사용
        DFS(v+1)        # 다음 원소로 넘어감

        ch[v]=0         # 0이면 사용하지 않음
        DFS(v+1)    

n = int(input(()))

ch=[0]*(n+1) # 원소 사용 여부 결정하는 check 변수
DFS(1)
