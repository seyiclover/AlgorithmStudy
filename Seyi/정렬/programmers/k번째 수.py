https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        s = command[0]
        e = command[1]
        i = command[2]
        tmp = array[s-1:e]
        tmp.sort()
        answer.append(tmp[i-1])
    return answer
