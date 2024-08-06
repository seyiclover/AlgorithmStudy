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
