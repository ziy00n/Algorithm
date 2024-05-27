# 백준 1920_수 찾기
# 이분탐색

import sys
input = sys.stdin.readline

n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(arr, target):
    L, R = 0, len(arr)-1
    while(L<=R):
        M = (L+R)//2
        if arr[M] == target:
            return 1
        elif arr[M] < target:
            L = M + 1
        else:
            R = M - 1
            
    return 0
    

for i in arr2:
    print(binary_search(arr1, i))