s = 'A+B*C-D/E'

stack = []
res = ''

for x in s:
    # 숫자인 경우 res 에 넣어준다.
    if x.isalpha():
        res+=x
    else:
        # 여는 괄호인 경우 stack 에 넣어준다.
        if x=='(':
            stack.append(x)
        
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                # 스택의 top에 있는 연산자를 res 에 넣어준다.
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            # 스택의 top에 있는 연산자가 여는 괄호가 아닐 때까지 res 에 넣어준다.
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            # 여는 괄호를 제거한다.
            stack.pop()

while stack:
    res+=stack.pop()

print(res)
