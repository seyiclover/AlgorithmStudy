# 구명보트의 최소 개수 구하기 >> 최대한 보트에 많은 사람 or 많은 몸무게 탑승 
# 가장 큰 무게와 작은 무게를 이분탐색으로 접근하면서 인덱스 갱신 

def titanic(n, m, passenger):
    passenger.sort(reverse=True)
    lt=0
    rt=len(passenger)-1
    cnt=0       # 보트의 수

    while lt<=rt:
        # 가장 무게가 무거운 사람 + 가벼운 사람 
        print(passenger[lt], passenger[rt])
        if passenger[lt]+ passenger[rt]<=m:
            cnt+=1
            lt+=1
            rt-=1
        else:
            cnt+=1
            lt+=1
    
    return cnt
    
n=5
m=140
passenger=[90, 50, 70, 100, 60]
# passenger=[45, 50, 60, 80, 70, 90, 100]
titanic(n, m, passenger)


# 정답 코드 
def titanic(limit, p):
    p.sort()
    cnt=0       # 보트의 수

    while p:        # p가 비어있지 않으면 참이돼서 작동 
        if len(p)==1:
            cnt+=1
            break
        if p[0]+p[-1]>limit:    # 한 사람이 타는 경우
            p.pop()
            cnt+=1
        else:                   # 두 사람이 타는 경우
            p.pop(0)
            p.pop()
            cnt+=1
    return cnt

# deque 활용 풀이
from collections import deque

def titanic(limit, p):
    p.sort()
    p=deque(p)
    cnt=0

    while p:
        if len(p)==1:
            cnt+=1
            break
        if p[0]+p[-1]>limit:
            cnt+=1
            p.pop()
        else:
            cnt+=1
            p.popleft()
            p.pop()
    return cnt
