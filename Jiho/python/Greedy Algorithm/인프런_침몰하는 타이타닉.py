n, m = map(int, input().split())
weights = list(map(int, input().split()))

mn = -1
cnt = 0 # 총 구출된 사람
boat = []
weights.sort(reverse=True)

for w in weights:

    if cnt >= n:
        break

    mw = weights[mn]
    if w + mw <= m:          # 가장 무거운 사람이 가장 가벼운 사람과 탈 수 있을 경우
        boat.append((w, mw)) # (가장 무거운 사람, 가장 가벼운 사람) 탑승
        cnt += 2  
        mn -= 1
    else: 
        boat.append(w) # 가장 무거운 사람 혼자 탐
        cnt += 1

print(len(boat))


'''

# 정답 풀이
# deque 활용

# deque 활용
from collections import deque

n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt = 0
p = deque(p)

while p: # p가 비어있으면 멈춤

    if len(p) == 1: # 한 명만 남으면
        cnt += 1
        break

    if p[0] + p[-1] > limit:
        p.pop() # 가장 무거운 사람만 out
        cnt += 1

    else:
        p.popleft()   # list에서 p.pop(0)
        p.pop()
        cnt += 1

print(cnt)

'''
