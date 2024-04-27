# 백준 2828_사과 담기 게임
# implementation, greedy

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

current = 1 # 바구니의 왼쪽 끝(시작위치)
ans = 0 # 바구니 이동거리의 최솟값

for i in range(j):
    x = int(input())
    # 사과가 바구니에 위치
    if current <= x <= current+m-1:
        continue
    # 바구니보다 왼쪽에 위치할 경우
    elif x < current:
        ans += current - x
        current -= current - x
    # 바구니보다 오른쪽에 위치할 경우
    else:
        ans += x - (current+m-1)
        current += x - (current+m-1)

print(ans)