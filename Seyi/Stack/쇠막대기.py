s= '()(((()())(())()))(())'
stack=[]
cnt=0
for i in range(len(s)):
    # 여는 괄호인 경우 stack 에 넣어준다.
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        # 레이저인 경우 stack 의 길이를 더해준다.
        if s[i-1]=='(':         
            cnt+=len(stack)
        # 쇠막대기의 끝인 경우 1을 더해준다.
        else:
            cnt+=1

print(cnt)
