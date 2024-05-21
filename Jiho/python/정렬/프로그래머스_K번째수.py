def solution(array, commands):
    
    answer = []
    
    for command in commands:
        
        first = command[0]
        second = command[1]
        third = command[2]
        
        tmp = array[first-1:second] # 2, 3, 4, 6
        tmp.sort()
        answer.append(tmp[third-1])
        
    return answer
