# 인프런 파이썬 알고리즘 문제풀이 입문(코딩테스트 대비)
# 1. 환경설정 및 K번째 약수 풀이

N, K = map(int, input().split())

nums = []
for i in range(1, N+1):
    if N % i == 0:
        nums.append(i)
    else:
        continue

if len(nums) >= K:
    print(nums[K-1])
else:
    print("-1")



'''
강의 답안: 

import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt +=1 
    if cnt == k:
        print(i)
        break
else:
    print(-1)


- K번째 약수를 찾자마자 출력하고 반복을 중단합니다. 이는 메모리를 효율적으로 사용하며, K번째 약수를 빠르게 찾을 수 있습니다. 
- 또한, K번째 약수를 찾기 전에 반복이 끝나면 자동으로 "-1"을 출력합니다.
- N이 클 때 더 나은 성능을 보일 수 있으며, 약수의 전체 리스트를 구성할 필요가 없어 추가 메모리가 절약됩니다.


'''
