import sys
input = sys.stdin.readline

n = int(input())

words=[]
for _ in range(n):
    words.append(input().strip('\n'))

words=list(set(words))
words.sort()
words.sort(key = lambda x :len(x))

for x in words:
    print(x)