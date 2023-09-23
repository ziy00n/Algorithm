#2775_부녀회장이 될테야

import sys
input = sys.stdin.readline

T = int(input()) # 테스트케이스

for i in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    arr = [i for i in range(1,n+1)] # 0층

    for b in range(k):
        for a in range(1,n):
            arr[a] += arr[a-1]         
    
    print(arr[n-1])