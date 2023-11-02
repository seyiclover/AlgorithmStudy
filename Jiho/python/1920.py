import sys

n = int(input())
A = set((map(int, sys.stdin.readline().split())))

m = int(input())
m_nums = list(map(int, sys.stdin.readline().split()))

for num in m_nums:
    if num in A:
        print(1)
    else:
        print(0)

'''
- 시간 초과 떠서 input() → sys.stdin.readline() 으로 했는데도 시간 초과
- A = list → A = set 으로 바꿨더니 성공
- 자료형에 따른 시간 복잡도
- 문제가 의도한 풀이: 이분 탐색(이진 탐색, binary search)
'''