N, M = map(int, input().split())
myDict = {}

for _ in range(N):
    host, pw = map(str, input().split())
    myDict[host]  = pw

for _ in range(M):
    search_host = input()
    print(myDict[search_host])
