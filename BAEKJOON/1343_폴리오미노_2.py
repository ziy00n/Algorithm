# 백준 1343_폴리오미노
# implementation

import sys
input = sys.stdin.readline

board = input().rstrip()

# replace() : 왼쪽부터 해당하는 문자열을 찾아서 치환
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)