# 백준 1244번 스위치 켜고 끄기
# implementation

import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))

student_num = int(input())

for _ in range(student_num):
    gender, gender_num = map(int, input().split())

    # 남학생
    if gender == 1:
        num = gender_num -1 # num: 0부터 시작하는 switch의 인덱스
        for i in range(num, n, num+1):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    
    # 여학생
    else:
        num = gender_num -1
        if switch[num] == 0:
            switch[num] = 1
        else :
            switch[num] = 0
    
        left, right = num-1, num+1
        while left >= 0 and right < n and switch[left] == switch[right]:
            if switch[left] == 0:
                switch[left], switch[right] = 1,1
            else :
                switch[left], switch[right] = 0,0
            left = left - 1
            right = right + 1

for i in range(0, n):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0: # 20개마다 줄바꿈(인덱스 19, 39 .. )
        print()