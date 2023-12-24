# 백준 1439_뒤집기
# 그리디

# import sys
# input = sys.stdin.readline
# sys 사용하면 실패 : 이유 찾아보기

S = input()
count = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

print((count + 1) // 2)