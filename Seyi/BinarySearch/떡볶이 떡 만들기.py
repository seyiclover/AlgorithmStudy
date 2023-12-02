# n, m 입력 
n, m = map(int, input().split())
# 떡의 길이 리스트 입력
array = list(map(int, input().split()))

# 이진탐색을 위한 범위인 절단기 높이를 1부터 가장 긴 떡의 길이까지 설정
lt=1
rt = max(array)

# 이진 탐색
while lt<=rt:
    mid=(lt+rt)//2
    total=0
    # 떡의 길이가 mid 보다 길 때 떡의 길이 추가
    for i in array:
        if i>mid:
            total+=i-mid
    # 누적된 떡의 양이 m과 같다면 반복문 종료
    if total==m:
        print(mid)
        break
    # 누적된 떡의 양이 m보다 크면 절단기 높이를 높여야 함
    elif total>m:
        lt=mid+1
    # 누적된 떡의 양이 m보다 작으면 절단기 높이를 낮춰야 함
    else:
        rt=mid-1
