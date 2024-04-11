# 백준 1138_한 줄로 서기
# implementation

import sys
input = sys.stdin.readline

n = int(input()) # 사람 수

# 키가 1인 사람부터 n인 사람까지 차례대로, 자기보다 키큰 사람이 왼쪽에 몇명 있었는지
arr = list(map(int, input().split())) # [2, 1, 1, 0]

result = [0] * n # [0, 0, 0, 0]

for i in range(n):
    cnt = 0
    for j in range(n):
        if result[j] == 0:
            cnt += 1
        if cnt == arr[i] + 1:
            result[j] = i+1
            break

print(*result)