# n개의 수를 오름차순으로 정렬한 다음 m이 몇번째인지 출력 

def binarysearch(numbers, m):
    # 오름차순이나 내림차순 정렬 
    numbers.sort()
    lt=0
    rt=len(numbers)-1
    while lt<=rt:
        mid=(lt+rt)//2
        if numbers[mid]==m:
            return mid+1    # 위치 정보는 index+1
        elif numbers[mid]>m:      # mid가 m보다 크면 왼쪽 범위를 탐색해야 하므로 mid 기준 오른쪽을 탐색 범위에서 제외
            rt=mid-1
        else:               # mid가 m보다 작으면 오른쪽 범위를 탐색해야 하므로 mid 기준 왼쪽을 탐색 범위에서 제외
            lt=mid+1

numbers=[23, 87, 65, 12, 57, 32, 99, 81]
binarysearch(numbers, 32)
