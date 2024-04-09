# 백준 16926_배열 돌리기 1
# implementation

import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split()) # n x m 배열을 r번 회전

arr = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * m for _ in range(n)] # r번 회전한 2차원 배열

# --아이디어 참고--
# deque 사용
# 껍데기별로 1차원으로 배열로 나열해서 회전한 뒤 다시 2차원 배열로 만들기
# deque에는 (0,0)부터 시계방향으로 상->우->하(거꾸로->좌(거꾸로) 로 넣어준다.
q = deque()
loops = min(n,m)//2 # 껍데기 개수(1차원 배열 개수)

# 한 껍데기마다 진행
for i in range(loops):
    q.clear()
    q.extend(arr[i][i : m-i]) # 위 한 행
    q.extend([row[m-1-i] for row in arr[i+1:n-1-i]]) # 오른쪽
    q.extend(arr[n-1-i][i:m-i][::-1]) # 아래 한 행
    q.extend([row[i] for row in arr[i+1:n-1-i]][::-1]) # 왼쪽
    q.rotate(-r) # 반시계로 r만큼 회전

    # 2차원 배열로 다시 모양 만들어주기
    for j in range(i, m-i): # 위 (y축 고정)
        result[i][j] = q.popleft()
    for j in range(i+1, n-1-i): # 오른쪽 (x축 고정)
        result[j][m-1-i] = q.popleft()
    for j in range(m-1-i, i-1, -1): # 아래 (y축 고정, 오른쪽 맨 끝 부터 왼쪽 끝까지 -1씩)
        result[n-1-i][j] = q.popleft()
    for j in range(n-2-i, i, -1): # 왼쪽 (x축 고정)
        result[j][i] = q.popleft()
    
for r in result:
    print(*r)