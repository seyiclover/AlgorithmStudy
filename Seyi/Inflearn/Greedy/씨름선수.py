# 지원자끼리 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자만 선발 

def competition(players):
    players.sort(key=lambda x: (x[0], x[1]))
    cnt=len(players) 

# 키순으로 오름차순 정렬했기 때문에 몸무게를 비교했을 때 뒷 지원자보다 적으면 탈락 
    for i in range(len(players)-1):
        if players[i][1] <= players[i+1][1]:
            cnt-=1

    return cnt

players = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]
competition(players)   


## 정답풀이
# 키순으로 내림차순 정렬 =>  키가 가장 큰 사람이 앞에 온다. 
# 몸무게로만 비교하면된다 => 뒷사람이 앞사람보다 몸무게가 크면된다. 
# 몸무게 최댓값만 갱신하면서 비교하면 효율적 

def competition(players):
    players.sort(reverse=True)      # key를 지정하지 않아도 첫번째 인자를 기준으로 정렬
    max_weight=0
    cnt=0
    for h, w in players:
        if w >= max_weight:
            max_weight=w
            cnt+=1              # 첫번째 사람은 무조건 counting 된다. 내림차순으로 정렬한 이유 

    return cnt

competition(players)
