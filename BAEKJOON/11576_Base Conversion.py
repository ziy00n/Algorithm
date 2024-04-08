# 백준 11576_Base Conversion
# implementation, 수학

import sys
input = sys.stdin.readline

a, b = map(int, input().split()) # A진법, B진법

m = int(input())

num = list(map(int, input().split()))

# A진법의 num -> 10진법 으로 바꾸기
# 뒤의 숫자부터 각 자리수에 1, A, A^2 .. 순서대로 곱한 후 더해서 10진수로 변환
n_10 = 0
num.reverse()
for i in range(m):
    # n_10 += num[m-1-i] * (a**i)
    n_10 += num[i] * (a**i)

# 10진법 -> B진법으로 바꾸기
n_b = []
while n_10 != 0:
    n_b.append(n_10 % b)
    n_10=n_10//b

print(*n_b[::-1])