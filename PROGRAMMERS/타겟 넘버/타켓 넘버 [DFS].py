# 프로그래머스 타겟 넘버
# 코딩테스트 고득점 Kit 깊이/너비 우선 탐색(DFS/BFS)
# DFS
# Lv.2


cnt = 0
def dfs(numbers, target, idx, cur_sum):
    global cnt
    if idx == len(numbers):
        if cur_sum == target:
            cnt += 1
        return
    
    dfs(numbers, target, idx + 1, cur_sum + numbers[idx])
    dfs(numbers, target, idx + 1, cur_sum - numbers[idx])

    
def solution(numbers, target):
    dfs(numbers, target, 0,0)
    return cnt