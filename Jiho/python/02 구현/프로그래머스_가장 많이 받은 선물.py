def solution(friends, gifts):
    answer = 0
    
    # 선물 지수
    scores = {friend:0 for friend in friends}
    
    for exchange in gifts:
        a, b = exchange.split() # 받은, 준
        scores[a] += 1
        scores[b] -= 1
    
    # 받을 선물
    get = {friend:0 for friend in friends}
    
    # 주고받은 수 계산
    # 2차원 리스트
    l = len(friends)
    exchange_record = [[0 for i in range(l)] for i in range(l)]
    
    for gift in gifts:
        a, b = gift.split()  # a b
        a_index = friends.index(a) # a, b, c
        b_index = friends.index(b)
        
        for i in range(l):
            for j in range(l): 
                if i==j: # 자기 자신에게는 선물 못 줌
                    exchange_record[i][j] -= 1
                    continue
                    
                elif i == a_index and j == b_index:
                        # a_index = 준 사람, b_index = 받은 사람
                        exchange_record[a_index][b_index] += 1

    # print(exchange_record)
    
    for i in range(l):
        for j in range(l):
            # 친구 이름
            a = friends[i]
            b = friends[j]
            
            if i >= j:  
                continue
                
            elif exchange_record[i][j] > exchange_record[j][i]: # a가 더 많이 줌
                get[a] += 1
            
            elif exchange_record[i][j] < exchange_record[j][i]: # b가 더 많이 줌
                get[b] += 1
                
            elif exchange_record[i][j] == exchange_record[j][i]: # 같음
                
                        if scores[a] > scores[b]: # a가 선물 지수 더 큼, 줘야함
                            get[a] += 1

                        elif scores[a] < scores[b]:
                            get[b] += 1


    print(get)
    
    answer = max(get.values())
    return answer
