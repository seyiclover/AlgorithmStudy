import sys
# 가능한 절단기의 길이 범위에서 이분탐색 

# 입력 
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 절단기의 길이는 1~20
lt, rt = 1, max(trees)

while lt <=rt:
    mid = (lt + rt) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree-mid
    # 자른 나무의 길이가 목표값 이상이면
    if cnt >= m:
        # 절단기 길이를 늘린다
        lt = mid + 1
    # 목표값 이하라면
    else:
        # 절단기 길이를 줄인다
        rt = mid - 1
        
print(rt)
