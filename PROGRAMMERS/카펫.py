# 프로그래머스 코딩테스트 고득점 Kit_카펫
# Lv.2
# 완전탐색

def solution(brown, yellow):
    all = brown + yellow
    
    for a in range(all, 2, -1):
        b = all / a
        if a >= b and all % a == 0:
            if (a-2)*(b-2) == yellow:
                return [a,b]