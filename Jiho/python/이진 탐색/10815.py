n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

nList = sorted(nList)

tmp = []
for num in mList:
    left = 0
    right = len(nList) - 1

    find = False
    while left <= right:

        mid = (left + right) // 2

        if num == nList[mid]:
            find = True
            tmp.append(1)
            break

        elif num > nList[mid]: # mid 보다 큼
            left = mid+1

        else:
            right = mid-1

    if not find:
        tmp.append(0)

for i in tmp:
    print(i, end=' ')