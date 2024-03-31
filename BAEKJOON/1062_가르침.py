# 백준 1062_가르침
# 백트래킹
'''
python3 -> 시간초과
pypy3 로 정답
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n개 단어, k개 글자 가르침

words = [set(input().rstrip()) for _ in range(n)]
# print(words)

learn = [False for _ in range(26)] # 알파벳 소문자
for i in ['a', 'n', 't', 'i', 'c']:
    learn[ord(i) - 97] = True
# print(learn)

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

# 백트래킹
# k개의 가르칠 알파벳 고르기 (조합)
result = 0
# arr = []
def dfs(index, cnt):
    global result
    if cnt == k:
        # k개 글자들의 조합 중에, 읽을 수 있는 단어의 최대개수 구하기
        result = max(result, check())
        return
    else:
        for i in range(index, 26): # 알파벳 index(시작 0 'a'부터 25까지), 조합이므로 내 앞은 탐색X
            if not learn[i]:
                learn[i] = True
                dfs(i+1, cnt+1)
                learn[i] = False

# n개 단어 중 읽을 수 있는 단어 개수 구하는 함수
def check():

    read_cnt = 0
    # words 의 단어 1개마다 이 과정 반복
    for word in words:
        flag = True
        for w in word:
            if not learn[ord(w) - 97]: # 가르침X 글자면
                flag = False
                break # 그 단어 더 돌 필요 X, 해당 단어는 못 읽음
        
        # 해당 단어의 글자들 살폈을 때 다 가르친 글자로 된 단어면
        if flag:
            read_cnt += 1 # 읽을수 있는 단어 수 +1
    return read_cnt


dfs(0, 5)
print(result)