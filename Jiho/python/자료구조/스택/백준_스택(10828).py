import sys

n = int(sys.stdin.readline().strip())
stack = []
for _ in range(n):
    command = sys.stdin.readline().strip()
    if command=='pop':
        if stack:
            print(stack[-1])
            a = stack.pop()
        else:
            print(-1)
    elif command=='size':
        print(len(stack))
    elif command=='empty':
        if stack: print(0)
        else: print(1)
    elif command=='top':
        if stack: print(stack[-1])
        else: print(-1)        
    else:
        num = command.split()[1]
        stack.append(num)
