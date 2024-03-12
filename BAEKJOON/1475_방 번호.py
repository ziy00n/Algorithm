# 백준 1475_방 번호
# implementation

import sys
input = sys.stdin.readline

n = input().rstrip() # n : 문자열

# 숫자의 개수를 그 숫자의 인덱스에 저장할 배열, 9는 nums[6]에 담으므로 [0] * 9 배열
nums = [0] * 9 

for i in range(len(n)):
    if n[i] == '6' or n[i] == '9': # nums[6] = 6의 개수 + 9의 개수
        nums[6] += 1
    else:
        nums[int(n[i])] += 1

if nums[6] % 2 == 0: # 짝수
    nums[6] = nums[6] // 2 # 6,9는 서로 뒤집어 사용가능 -> 2로 나눈 몫이 필요한 세트 수
else: # 홀수
    nums[6] = (nums[6] + 1) // 2

print(max(nums))