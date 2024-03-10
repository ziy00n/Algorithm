# 백준 2563_색종이
# implementation

# [ 100 * n - 겹치는 넓이 ] 풀이는 색종이 3개 겹칠 때, 안 겹칠 때 등 경우 다 따지기 어려움
# 도화지를 (1 * 1) 정사각형 100개의 집합으로 가정 후 시작
import sys
input = sys.stdin.readline

n = int(input()) # 색종이 수

arr = [[0 for col in range(101)] for row in range(101)] # 101 * 101 도화지를 0으로 초기화 (arr의 요소 : 도화지 한 칸 의미)

# 받은 좌표에 맞게 10*10 정사각형 1로 채우기
for _ in range(n):
    x, y = map(int, input().split())
    for row in range(x, x+10):
        for col in range(y, y+10):
            arr[row][col] = 1

result = 0

for i in arr:
    result += i.count(1) # arr 내의 1의 개수 count 
    # result += sum(i) # 1이 아닌 부분이 0이므로 모두 더하면 넓이 구할 수 있음
print(result)