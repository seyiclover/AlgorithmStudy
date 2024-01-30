def DFS(L, sum):    # L: 트리의 레벨/group 인덱스, sum: 부분집합의 원소의 합
    global switch
    if switch: return
    # 종료지점 출력
    if L==n:
        # 부분집합 원소의 합 저장
        if sum == total-sum:
            print("YES")
            # 코드 종료
            switch = 1

    # 사용할지 안할지 여부 결정    
    else:
        DFS(L+1, sum+group[L])
        DFS(L+1, sum)

if __name__=="__main__":
    switch = 0
    n=int(input())
    group = list(map(int, input().split())) 
    total = sum(group)

    DFS(0, 0)
    if switch==0: print('NO')