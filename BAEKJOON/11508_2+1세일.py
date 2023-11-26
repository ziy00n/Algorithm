import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
	a = int(input())
	arr.append(a)
	
arr.sort(reverse=True)
ans = 0

for i in range(n):
	if (i+1) % 3 != 0:
		ans += arr[i]

print(ans)