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
    lt=9
    rt=sum(songs)
    res=0
    while lt<=rt:
        mid=(lt+rt)//2
        if  count_DVD(mid) <= m:  
            rt=mid-1
            res=mid         # 조건을 만족하는 mid를 res에 저장
        else:
            lt=mid+1
    return res
  
songs=[1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 3

min_DVD_size(songs, m)
