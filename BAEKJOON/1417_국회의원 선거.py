# 백준 1417_국회의원 선거
# implementation

n = int(input())
dasom = int(input())
vote = []

for _ in range(n-1):
    vote.append(int(input()))

cnt = 0
vote.sort(reverse = True)

if n == 1:
    print(0)

else:
    while vote[0] >= dasom:
        dasom += 1
        vote[0] -= 1
        cnt += 1
        vote.sort(reverse = True)
    print(cnt)