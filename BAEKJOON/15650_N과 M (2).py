# 백준 15650번 N과 M (2)
# 백트래킹, 조합

# 1 ~ n  까지의 자연수
# 중복없이 m개 고른 수열, 오름차순
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

arr = []
def dfs(index):
    if len(arr) == m:
        print(*arr)
    else:
        for i in range(index, len(nums)):
            arr.append(nums[i]) # nums가 오름차순이므로 arr도 오름차순으로 저장됨.
            dfs(i+1)
            arr.pop()
dfs(0)