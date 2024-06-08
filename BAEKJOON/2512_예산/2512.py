# 백준 2512_예산
# 이분탐색

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

nums.sort()

answer = 0

def binary_search(nums, M):
    L = 1
    R = max(nums)

    while(L <= R):
        mid = (L+R)//2
        total = 0
        
        for i in nums:
            if i <= mid:
                total += i
            else:
                total += mid

        if total <= M:
            L = mid + 1
            answer = mid
        else:
            R = mid - 1
            
    return answer

print(binary_search(nums, M))