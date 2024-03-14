# 백준 25206_너의 평점은
# implementation

# ObjectOrientedProgramming1 3.0 A+
# 과목명, 학점, 평점(A+ = 4.5)
# 전공평점 : 전공과목별 (학점 * 과목평점)의 합 / 학점의 총합

import sys
input = sys.stdin.readline

dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
time = []
grade = []
for _ in range(20):
    x, y , z = input().split()
    if z != 'P':
        time.append(float(y))
        grade.append(dic[z])

sum_top = 0
for i in range(len(time)):
    sum_top += time[i] * grade[i]

print(round(sum_top / sum(time), 6))

'''
# 2번째 생각해본 방법
# 메모리 1번 방법과 같음, 시간 4ms 더 걸림

import sys
input = sys.stdin.readline

dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
top=0
bottom =0

for _ in range(20):
    info = input().split()
    if info[2] != 'P':
        y = float(info[1]) # 학점 (3.0)
        z = dic[info[2]] # 평점(A+ = 4.5)
        # print(y)
        # print(z)
        #print(y*z)
        top += y * z
        bottom += y

# print(top)
# print(bottom)
print(round(top / bottom, 6))
'''