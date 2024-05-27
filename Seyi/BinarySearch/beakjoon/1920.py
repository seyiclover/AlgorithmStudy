# set 함수와 in 메서드 활용 풀이
n = int(input())
n_lst = set(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

for x in m_lst:
    if x in n_lst:
        print(1)
    else:
        print(0)   

# 이분탐색 적용 
n = int(input())
list_n = list(map(int, input().split()))
list_n.sort()
m = int(input())
list_m = list(map(int, input().split()))

def binary_search(data,target):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return mid+1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for target in list_m:
    if binary_search(list_n,target):
        print(1)
    else:
        print(0)
