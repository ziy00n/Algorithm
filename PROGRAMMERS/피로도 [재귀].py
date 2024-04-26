# 프로그래머스_피로도
# Lv.2
# 완전탐색
# - 재귀를 이용한 풀이 - # 

def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]
    return exploring(k, dungeons, visited, 0)
    
max_cnt = 0
def exploring(k, dungeons, visited, cnt):
    global max_cnt
    
    for i in range(len(dungeons)):
        max_cnt = max(max_cnt, cnt)
        min_f, f = dungeons[i]
        
        if visited[i] == False and k >= min_f:
            visited[i] = True
            exploring(k-f, dungeons, visited, cnt+1)
            visited[i] = False
            
    return max_cnt