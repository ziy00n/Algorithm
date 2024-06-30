# 백준 15723_n단 논법
# 플로이드-워셜

n = int(input())
INF = int(1e9)
graph = [[INF for i in range(26)] for i in range(26)]

for _ in range(n):
    arr = input().split()
    s = ord(arr[0]) - ord('a') # 숫자로 변환
    e = ord(arr[2]) - ord('a')
    graph[s][e] = 1

for k in range(26):
    for a in range(26):
        for b in range(26):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

m = int(input())

for _ in range(m):
    arr = input().split()
    s = ord(arr[0]) - ord('a')
    e = ord(arr[2]) - ord('a')
    if graph[s][e] < INF:
        print('T')
    else:
        print('F')