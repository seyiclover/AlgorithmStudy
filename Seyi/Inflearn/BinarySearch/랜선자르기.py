# 랜선자르기_이분탐색을 적용 
# k개의 랜선을 가지고 있고, n개의 랜선을 만들어야 한다.
# k개의 랜선을 잘라서 n개의 랜선을 만들 수 있는 최대 랜선의 길이를 구하라.

def CuttingLine(lines, n):
    lines.sort()            # 오름차순 정렬
    lt =1                   # 정답이 될 수 있는 범위를 lt~rt로 지정 
    rt = lines[-1]          # rt는 주어진 랜선 중 최대 길이로 지정
    while lt<=rt:
        mid=(lt+rt)//2
        cnt=0
        for line in lines:
            cnt += line//mid    # cnt: 주어진 랜선들을 mid의 길이만큼 나눴을 때 만들어진 랜선의 개수
        if cnt==n:              # cnt=n 이라면 필요한 랜선의 개수를 충족했으므로 mid가 랜선의 최대 길이가 된다. 
            return mid
        elif cnt<n:             # cnt가 n을 충족하지 않는다면 길이를 더 잘게 잘라야 하므로 rt를 mid-1로 이동 
            rt=mid-1            # -1을 하는 이유는? 기존의 mid는 답에 포함되지 않기 때문
        else:
            lt=mid+1        

lines=[802,743,457,539]
CuttingLine(lines, 11)
