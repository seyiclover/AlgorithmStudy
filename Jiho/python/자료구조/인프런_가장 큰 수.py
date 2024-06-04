num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m>0 and stack[-1]<x: # stack이 비어있지 않고 마지막에 stack에 들어간 수가 지금 수보다 작음
        stack.pop() # 마지막에 들어간 숫자 pop
        m -= 1
    stack.append(x)
if m!=0: # 더 지워야함
        stack = stack[:-m] # 뒤쪽 m개의 숫자 삭제

res = ''.join(map(str, stack))
print(res)

