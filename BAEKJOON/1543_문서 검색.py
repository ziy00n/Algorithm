# 백준 1543_문자 검색
# 문자열

import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

i = 0
cnt = 0
while i < len(a):
    if a[i:i+len(b)] == b:
        i += len(b)
        cnt += 1
    else :
        i += 1
print(cnt)