# 후위식 연산

a = input()
stack = [] 

def cal(num1, num2, c):
    if c == '+':
        return num2 + num1
    elif c == '-':
        return num2 - num1
    elif c == '*':
        return num2 * num1
    elif c == '/':
        return num2 / num1
    
for n in a:
    if n.isdecimal():
        stack.append(n)
    else:
        n1 = int(stack.pop()) # stack 최상단
        n2 = int(stack.pop())
        stack.append(cal(n1, n2, n))  

print(stack[0])
