# 풀이 1 
def solution(number, k):
    answer = []

    for i in number:
        if len(answer) == 0:
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if len(answer) == 0 or k <= 0:
                    break
        answer.append(i)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

# 풀이 2 
def solution(number, k):
    stack = []
    for x in number:
        while stack and k>0 and stack[-1]<x:
            stack.pop()
            k-=1
        stack.append(x)
    if k != 0:      # k개를 다 제거하지 못했는데 반복문이 종료된 경우
        stack=stack[:-k]   
 
    return ''.join(stack)
