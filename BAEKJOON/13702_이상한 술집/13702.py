# 백준 13702_이상한 술집
# 이분탐색

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 한 명한테 줄 수있는 최대 막걸리양 = mid

arr = [int(input()) for _ in range(N)]

answer = 0
def binary_search(arr):
    L = 1
    R = max(arr)
    
    while(L <= R):
        mid = (L+R)//2
        cnt = 0
        for ml in arr:
            cnt += (ml//mid)
            
        if cnt >= K:
            answer = mid
            L = mid + 1
        else:
            R = mid - 1
    return answer

print(binary_search(arr))