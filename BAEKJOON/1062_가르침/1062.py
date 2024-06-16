# 백준 1062_가르침
# 백트래킹

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

words = [list(input().rstrip()) for _ in range(n)]
alphabet = [0] * 26

for letter in ['a','n','t','i','c']:
    alphabet[ord(letter)-ord('a')] = 1


if k<5:
    print(0)
    exit()

elif k == 26:
    print(n)
    exit()
  
answer = 0

def dfs(n, cnt):
    global answer
    
    if cnt == (k-5):
        word_cnt = 0
        for word in words:
            flag = True
            for w in word:
                if alphabet[ord(w)-ord('a')] == 0:
                    flag = False
                    break
            if flag == True:
                word_cnt += 1
        answer = max(answer, word_cnt)
        return

    for i in range(n, 26):
        if alphabet[i] == 0:
            alphabet[i] = 1
            dfs(i, cnt+1)
            alphabet[i] = 0

        
dfs(0, 0)
print(answer)