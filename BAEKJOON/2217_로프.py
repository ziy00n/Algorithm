import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

weight = 0

for i in range(n-1, -1, -1):
    weight = max(weight, arr[i] * (n-i))

print(weight)
