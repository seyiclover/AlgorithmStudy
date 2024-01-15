# 큐 임포트
from collections import deque

n, k = 8, 3
princes = [i for i in range(1, n+1)]
 # 큐에 왕자들을 넣는다. 
princes = deque(princes)

# 왕자가 1명만 남을 때까지 반복
while len(princes) > 1:
    # k번 반복 
    for i in range(k-1):
        princes.append(princes.popleft())
    princes.popleft()

print(princes.pop())
