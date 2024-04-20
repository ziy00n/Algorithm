# 백준 1065_한수
# 완전탐색

N = int(input())
result = 0

for i in range(1, N+1):
    if i <= 99:
        result += 1
    else:
        arr = list(map(int, str(i)))
        # print(arr)
        if arr[0] - arr[1] == arr[1] - arr[2]:
            result += 1

print(result)        