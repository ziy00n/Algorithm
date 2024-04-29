# 백준 16439_치킨치킨치킨
# 완전탐색

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

favorite = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for c1, c2, c3 in combinations(range(m), 3):
    member_max_sum  = 0
    for i in range(n):
        member_max_sum += max(favorite[i][c1], favorite[i][c2], favorite[i][c3])
    max_sum = max(max_sum, member_max_sum)

print(max_sum)