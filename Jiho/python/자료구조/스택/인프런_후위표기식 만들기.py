import sys
sys.stdin=open("input.txt", 'r')
a = input() # 중위식
stack = []
res = '' # 출력
for x in a:
    if x.isdecimal(): # 숫자이면 출력
        res+=x 
    else: # 연산자이면
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'): # 스택 상단이 *, / (우선순위 같음)
                res+=stack.pop() # 스택 상단 자료를 res에 누적
            stack.append(x)
        elif x=='+' or x=='-':  
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)

