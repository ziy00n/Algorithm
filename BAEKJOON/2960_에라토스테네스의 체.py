# 백준 2960_에라토스테네스의 체
# implementation

n, k = map(int, input().split())

num = []
for i in range(2, n+1):
    num.append(i)

del_num = []
while num:
    x = min(num)
    for i in num:
        if i % x == 0:
            num.remove(i)
            del_num.append(i)

print(del_num[k-1])