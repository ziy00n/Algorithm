# 백준 1541_잃어버린 괄호
# 그리디

arr = input().split('-')

sum = 0
for i in arr[0].split('+'):
    sum += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)