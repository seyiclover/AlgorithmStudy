import sys
from collections import deque

n, m = map(int, input().split()) # 환자 수, m번째 환자
patients = list(map(int, input().split()))
patients = [(i, n) for i, n in enumerate(patients)]
dq = deque(patients)

patients = [(i, n) for i, n in enumerate(patients)]
dq = deque(patients)

cnt = 0
target = -1


while target != m:
    mx = max([i[1] for i in dq])
    cur = dq.popleft()
    if cur[1] != mx:
        dq.append(cur)
    else:
        target = cur[0] # 진료받은 사람
        cnt += 1

print(cnt)
