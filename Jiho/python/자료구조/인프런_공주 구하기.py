# que
# FIFO

import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, k = map(int, input().split())

dq = list(range(1, n+1))
dq = deque(dq) # deque 자료구조
while dq: # que가 비면 멈춤
    for _ in range(k-1): # 앞에거 pop -> 뒤에 append
        cur = dq.popleft() # 앞에거 pop
        dq.append(cur) # 뒤에 append
    dq.popleft() # k번째 사람은 그냥 사라짐
    if len(dq)==1:
        print(dq[0])
        dq.popleft() # while dq 거짓 -> 멈춤
