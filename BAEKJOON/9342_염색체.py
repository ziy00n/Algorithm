# 백준 9342_염색체
# 문자열

import sys
input = sys.stdin.readline
import re

n = int(input())
p = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(n):
    test = input()
    if p.match(test)==None:
        print('Good')
    else:
        print('Infected!')