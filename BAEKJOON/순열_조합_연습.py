'''
다중 for문 방식
'''

# nums=[1,2,3,4]
# count = 0 # 답
#순열 
# print("순열: ")
# for i in range(len(nums)): # 숫자 4개(i, j, k, l) 순열 4P4 = 24
#     for j in range(len(nums)):
#         if j != i:  # i와 j가 다를 때만 실행
#             for k in range(len(nums)):
#                 if k != i and k != j:
#                       for l in range(len(nums)):
#                           if l != k and l != i and l != j:
#                               print(nums[i], nums[j], nums[k], nums[l])
#                               count += 1
# print(count)

# 조합
# print("조합 : ")                       
# for i in range(len(nums)): # 4C4 = 1
#     for j in range(i + 1, len(nums)):
#         for k in range(j + 1, len(nums)):
#             for l in range(k + 1, len(nums)):
#                 print(nums[i], nums[j], nums[k], nums[l])
#                 count += 1

# print(count)

# numsB = [1,2,3]

# 중복 순열 3파이3 = 3^3 = 27
# for i in range(len(numsB)):
#     for j in range(len(numsB)):
#         for k in range(len(numsB)):
#             print(numsB[i], numsB[j], numsB[k])
#             count += 1

# print(count)

# 중복 조합 3H3 = 10
# for i in range(len(numsB)):
#     for j in range(i, len(numsB)):
#         for k in range(j, len(numsB)):
#             print(nums[i], nums[j], nums[k])
#             count += 1
# print(count)


'''
백트래킹 DFS 방식
'''
# 순열 
nums = [1,2,3]
arr = []
count2 = 0
goal = 3 # 3P3 = 6 
def dfs():
    global count2
    if len(arr) == goal:
        print("answer: ")
        print(*arr)
        count2 += 1
    else:
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
                print("appended arr: ")
                print(arr)
                dfs()
                arr.pop()
                print("poped arr: ")
                print(arr)
dfs()

# print(count2)

# # 조합 numsCgoal
# nums = [1,2,3]
# arr = []
# count2 = 0 
# goal = 3 # 중복없이 조합으로 만들고 싶은 숫자 개수
# def dfs(index):
#     global count2
#     if len(arr) == goal:
#         print(*arr)
#         count2 += 1
#     else:
#         for i in range(index, len(nums)):
#             arr.append(nums[i])
#             dfs(i+1)
#             arr.pop()
# dfs(0)
# print(count2)

# 중복순열 3파이3 = 3^3 = 27
# nums = [1,2,3]
# arr = []
# count2 = 0 
# goal = 3 # 중복 포함 순열 만들고 싶은 숫자 개수

# def dfs():
#     global count2
#     if len(arr) == goal:
#         print(*arr)
#         count2 += 1
#     else:
#         for i in range(len(nums)):
#             arr.append(nums[i])
#             dfs()
#             arr.pop()
# dfs()
# print(count2)

# # 중복 조합 3H3 = 10
# nums = [1,2,3]
# arr = []
# count2 = 0 
# goal = 3 # 중복 포함 조합 만들고 싶은 숫자 개수
# def dfs(index):
#     global count2
#     if len(arr) == goal:
#         print(*arr)
#         count2 += 1
#     else:
#         for i in range(index, len(nums)):
#                 arr.append(nums[i])
#                 dfs(i)
#                 arr.pop()

# dfs(0)
# print(count2)

# # 원순열
# nums = [1,2,3,4]
# arr = []
# arr.append(nums[0]) # 첫번째 숫자 고정
# count2 = 0
# def dfs():
#     global count2
#     if len(arr) == 4:
#         print(*arr)
#         count2 += 1
#     # print(*arr)
#     # answer.append(arr[:])
#     else:
#         for i in range(1, len(nums)): # 모든 요소 다 두번째 숫자부터 끝까지
#                 if nums[i] not in arr: # 중복되지 않는 숫자로
#                     arr.append(nums[i]) # arr에 넣기
#                     dfs() # 재귀 호출
#                     print(arr)
#                     arr.pop()
#                     print(arr)

# dfs()
# print(count2)