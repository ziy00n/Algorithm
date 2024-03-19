# 백준 1992번 쿼드트리
# 분할정복

import sys
input = sys.stdin.readline

n = int(input())

video = []
for _ in range(n):
    video.append(list(map(int, input().rstrip())))

def check(y, x, size):
    global graph
    for i in range(y, y + size):
        for j in range(x, x+ size):
            if  video[i][j] != video[y][x]:
                return False
    return True

result = ""
def divide(y, x, size):
    global result
    if check(y, x, size):
        result += str(video[y][x])
    else:
        new_size = size//2
        result += "("
        for i in range(2):
            for j in range(2):        
                divide(y + new_size*i, x + new_size*j, new_size)
        result += ")"
        
divide(0, 0, n)
print(result)