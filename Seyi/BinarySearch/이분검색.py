n, m = map(int, input().split())
n_lst = list(map(int, input().split()))
n_lst.sort()    # 오름차순 정렬 

s = 0
e = n-1
while s<=e:     # s가 e보다 커지면 탐색 종료
    mid = (e+s) // 2
    if  m == n_lst[mid]:    # 중간값과 m이 일치하면 mid 인덱스 출력
        print(mid+1) 
        break
    elif n_lst[mid] > m:    # 중간값이 m보다 크면 탐색 지점을 앞구간으로 축소 
        e = mid - 1
    else:                   # 중간값이 m보다 작으면 탐색 지점을 뒷구간으로 축소
        s = mid + 1
