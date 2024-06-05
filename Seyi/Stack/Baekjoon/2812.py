n, k = map(int, input().split())
num = input()

stack = []
for x in num:
    while k >0 and len(stack) != 0 and stack[-1] < x:
        stack.pop()
        k -= 1
    stack.append(x)

if k!=0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
