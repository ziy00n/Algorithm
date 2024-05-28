# 백준 2644_촌수계산
# DFS

import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람수
p1, p2 = map(int, input().split())
m = int(input())

tree = dict()
seen = set()

for i in range(1, n+1):
    tree[i] = []

# 부모-자식관계
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
    
flag = False    
def dfs(p1, p2, cnt):
    global flag
    
    if p1 == p2:
        print(cnt)
        flag = True
    
    # p1 != p2 면
    seen.add(p1)
    items = tree[p1]
    
    for item in items:
        if item not in seen:
            dfs(item, p2, cnt+1) #**

 
dfs(p1, p2, 0)
    
if flag == False:
    print(-1)