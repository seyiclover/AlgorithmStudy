from collections import deque

# n: 환자 수, m:진료 순서를 구해야하는 환자의 번호
n, m = map(int, input().split())

# 환자의 위험도 입력
# dq = list(map,(int, input().split()))
# 들어온 순서대로 환자 인덱싱
dq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(dq)
cnt=0

while True:
    cur=Q.popleft()
    # cur보다 큰 값이 Q에 존재하는지 확인
    if any(cur[1]<x[1] for x in Q):      # 예시 cur = (0, 60)   # if any: 단 한개라도 참이면 조건문 참 
        Q.append(cur)
        print(Q)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)
