# 백준 2422_한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 완전탐색

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

icecream = [[False for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split()) # 섞어먹으면 안되는 아이스크림 번호
    icecream[a-1][b-1] = True
    icecream[b-1][a-1] = True

result = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not icecream[i][j] and not icecream[i][k] and not icecream[j][k]:
                result += 1

print(result)