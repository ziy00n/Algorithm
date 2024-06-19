# 백준 1759_암호 만들기
# DFS

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(map(str, input().split())) # c문자 종류
arr.sort()
vowel = ['a','e','i','o','u']

def dfs(k, lst):
    a = 0 # 자음 개수
    b = 0 # 모음 개수
    if len(lst) == L:
        for i in lst:
            if i in vowel:
                b += 1
            else:
                a += 1
        if b >= 1 and a >=2:
            print(''.join(lst))
            return
        return

    for i in range(k, len(arr)):
        dfs(i+1, lst+[arr[i]])

dfs(0, [])