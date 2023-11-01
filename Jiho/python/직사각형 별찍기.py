n, m = map(int, input().strip().split(' '))

# 1
for i in range(m):
    for j in range(n):
        print('*', end='')
    print('')

# 2
for i in range(m):
    print('*'*n, end='')
