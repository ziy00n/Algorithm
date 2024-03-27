# 백준 1051_숫자 정사각형
# implementation

# NxM 크기의 직사각형
# 각 칸에 한자리 숫자
# 직사각형에 꼭짓점에 쓰여있는 수가 모두 같은 가장 큰 정사각형
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

s = min(n, m)
area = 0
for y in range(n):
    for x in range(m):
        # 이동 범위 : 0 ~ 최대 s-1 (인덱스)
        for k in range(s):
            # m범위 넘지 않고, n범위 넘지 않게 탐색
            if (x+k) < n and (y+k) < m:
                if arr[y][x] == arr[y+k][x] == arr[y][x+k] == arr[y+k][x+k]:
                    area = max(area, (k+1)**2)

print(area)