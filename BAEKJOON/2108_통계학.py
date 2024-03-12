# 백준 2108_통계학
# implementation

import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

# 1. 산술평균
# sum() :  Iterable 자료형의 엘리먼트들의 값을 모두 더하는 연산
print(round(sum(nums)/n)) # round() : 실수 반올림

# 2. 중앙값
nums.sort() # 오름차순 정렬
#print(nums[(len(nums)-1) // 2])
print(nums[n//2]) # // : int형 나눗셈(몫) , / : float형 나눗셈

# 3. 최빈값
# 최빈값 - 풀이 참조
# *딕셔너리 사용*

dict = {} # key:value = 숫자 : 빈도수

for a in nums: # 오름차순 정렬된 nums
    if a not in dict:
        dict[a] = 1
    else: 
        dict[a] += 1

max_cnt = max(dict.values()) # 빈도수 중 최대값
max_arr = [] # 최빈값 숫자를 저장할 배열

for i in dict: # 빈도수 딕셔너리에서
    if max_cnt == dict[i]: # 빈도수(dict[i])가 max_cnt 랑 같으면
        max_arr.append(i) # 그 숫자(key) i를 max_arr에 담기

# max_arr.sort() # 정렬된 nums로 dict 만들었으므로 dict도 정렬되어있고, max_arr도 정렬 순서로 저장됐으므로 sort() 안해도 됨.

if len(max_arr) > 1: # 최빈값이 여러개 일 떄
    print(max_arr[1]) # 두번째로 작은 값 출력
else: # 최빈값을 갖는 숫자를 담은 max_arr길이가 1이면
    print(max_arr[0]) # 배열의 숫자 출력

# 4. 범위
print(abs(nums[-1]-nums[0]))

'''
# 3. 최빈값
# count = 0

# for i in range(n):
#     for j in range(i+1, n):
#         cnt.append([i, i])

# for i in nums:
#     cnt.append([nums.count(i), i])
# print(cnt)


# cnt.sort(reverse = True) # 값마다 개수를 내림차순 정렬
# print(cnt)
# print(cnt[0][1]) 
# print(cnt[0][0]) #
'''