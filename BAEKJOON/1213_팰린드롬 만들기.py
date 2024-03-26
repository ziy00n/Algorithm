# 백준 1213_팰린드롬 만들기
# implementation

import sys
from collections import Counter
input = sys.stdin.readline

word = list(input().rstrip())
word.sort() # 사전 순 오름차순 정렬

# Counter 함수 : 딕셔너리 형태
# 각 항목을 키로 해서 개수를 알려줌
counter_word = Counter(word) 
# print(counter_word)

# word의 알파벳중에 갯수가 홀수인 것이 2개 이상이면 팰린드롬 X
# 홀수개인 알파벳은 가운데에 들어가야하므로 따로 저장하고 word에서 1개를 삭제
center = ''
for w in counter_word:
    if len(center) > 1:
        break
    if counter_word[w] % 2 != 0:
        center += w
        word.remove(w)
    
result = ''
if len(center) > 1:
        print("I'm Sorry Hansoo")
else:
    for i in range(0, len(word), 2):
        result += word[i]
    print(result + center + result[::-1]) # [::-1] : 문자열 뒤집기(리스트, 튜플에도 사용 가능)