# 프로그래머스_피로도
# Lv.2
# 완전탐색

from collections import deque
from copy import deepcopy

def solution(k, dungeons):
    stack = deque()
    visited = [False for _ in range(len(dungeons))]
    maxCount = 0
    stack.append([k, visited])
    
    while stack:
        k, visited = stack.pop()
        maxCount = max(maxCount, visited.count(True)) 
    
        for i, dungeon in enumerate(dungeons):
            min_p, p = dungeon
            
            # if visited[i]:
            #     continue
            # if k < min_p:
            #     continue

            if visited[i] == False and k >= min_p:
                temp_visited = deepcopy(visited)
                temp_visited[i] = True
                stack.append([k-p, temp_visited])
                
    return maxCount
                  