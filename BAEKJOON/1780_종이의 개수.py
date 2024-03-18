# 백준 1780번 종이의 개수
# 분할정복

import sys
input = sys.stdin.readline

n = int(input()) # N은 3의 제곱

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

# 모두 같은 숫자로 채워진 종이인지 판별하는 함수
def check(y, x, size): # graph[y][x] 부터 시작하는 n = size인 정사각형 조사
    num = paper[y][x] # 체크하려는 잘린 종이의 첫번째 숫자
    for i in range(y, y+size):
        for j in range(x, x+size):
            if paper[i][j] != num: # 해당 종이 안에서 다른 숫자가 있으면
                return False
    return True

cnt = [0, 0, 0]

# 종이 9등분하고 개수 세는 함수
def divid_paper(y, x, size): 
    if check(y, x, size): # 자르지 않고 정사각형 종이로 사용가능하면(True), 각각 종이 개수 +1
        if paper[y][x] == -1:
            cnt[0] += 1
        elif paper[y][x] == 0:
            cnt[1] += 1
        else:
            cnt[2] += 1
    else: 
        next_size = size // 3 # 새로운 정사각형 크기
        for i in range(3): # 9등분
            for j in range(3):
                divid_paper(y + next_size*i, x + next_size*j, next_size) # 재귀로 위 과정 반복
        

divid_paper(0, 0, n)

print(cnt[0]) 
print(cnt[1])
print(cnt[2])