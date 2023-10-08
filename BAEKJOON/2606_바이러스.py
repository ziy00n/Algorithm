import sys

n = int(sys.stdin.readline())  # 컴퓨터의 개수
m = int(sys.stdin.readline())  # 쌍의 개수

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 서로 각자 연결되어있기 때문에 양쪽 다 넣어준다 ex) 1노드와 2가 연결되어 있으면 2노드랑 1노드와도 연결

# print(graph)

result = 0
visited = [0] * (n + 1)


def dfs(start):
    global result
    visited[start] = 1
    for j in graph[start]:
        if visited[j] == 0:  # 방문하지 않은 노드라면 
            result += 1
            dfs(j)  # 반복 재귀


dfs(1)
print(result)