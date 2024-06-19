# 백준 1302_베스트셀러
# 자료구조, 문자열

import sys
input = sys.stdin.readline
n = int(input())

book = {}

for _ in range(n):
    title = input().rstrip()
    if title not in book:
        book[title] = 1
    else:
        book[title] += 1

print(sorted(book.items(), key=lambda x : (-x[1], x[0]))[0][0])