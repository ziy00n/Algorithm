# 백준 1748_수 이어 쓰기 1
# implementation

import sys
input = sys.stdin.readline

n = input().rstrip() # EX) n='120', len(n) = 3

result= 0
for i in range(1, len(n)):
    result +=  9 * (10 ** (i-1)) * i
# 가장 높은 자릿수의 숫자 개수 * 길이
# EX) n='120', len(n) = 3
# 100 ~120 까지 개수 * 길이
# 120-100+1= 21, 길이=3, 21 * 3 = 63
result += (int(n) - (10 ** (len(n)-1)) + 1) * len(n)

print(result)

# 시간초과된 풀이
# 문제의 n의 범위가 1억이하. 시간제한 0.5초
# n 이 1억일 때, for문을 1억번 연산해야함
# 1초 당 1억번 연산 => 시간초과
'''
n = int(input())
result = ""
for i in range(1, n+1):
    result += str(i)
print(len(result))
'''