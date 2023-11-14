def count_DVD(capacity):
    total=0                  # DVD 하나에 누적된 노래의 길이
    cnt=1                   # 노래를 담는 데 필요한 DVD 개수 
    for song in songs:
        if total+song > capacity:
            cnt+=1
            total=song
        else:
            total+=song
    return cnt


def min_DVD_size(songs, m):
    lt=1
    rt=sum(songs)
    maxx=max(songs)     # mid>=maxx를 설정하지 않으면 mid가 0이 되는 경우가 생긴다. mid 가 계속 작아져도 lt<=rt 조건을 만족하기 때문에(m=9인 경우)
    res=0
    while lt<=rt:
        mid=(lt+rt)//2
        if  mid>=maxx and count_DVD(mid) <= m:  
            rt=mid-1
            res=mid         # 조건을 만족하는 mid를 res에 저장
        else:
            lt=mid+1
    return res
  
songs=[1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 9

min_DVD_size(songs, m)
