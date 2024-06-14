# 백준 2961_도영이가 만든 맛있는 음식
# 백트래킹

import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

answer = int(1e9)
def dfs(k, S, B):
    global answer
    
    if B != 0: # 재료 하나라도 선택(B가 초기값인 0이 아니면)
        answer = min(answer, abs(S-B))
    
    for i in range(k, n):
        dfs(i+1, S * arr[i][0], B + arr[i][1])
        
dfs(0, 1, 0)
print(answer)