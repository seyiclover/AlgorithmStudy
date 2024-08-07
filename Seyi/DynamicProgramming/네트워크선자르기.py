# Top-down
d = [0] * 50

def cutLine(x):
    if x == 1 or x == 2:
        return x
    if d[x] != 0:
        return d[x]
    else:
        d[x] = cutLine(x-2) + cutLine(x-1)
        return d[x]

if __name__=="__main__":
    n=int(input())
    d = [0] * (n+1)
    print(cutLine(n))

# Bottom-up 
n = int(input())
d = [0] * (n+1)
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    if d[i] ==0:
        d[i] = d[i-1] + d[i-2]

print(d[n])
