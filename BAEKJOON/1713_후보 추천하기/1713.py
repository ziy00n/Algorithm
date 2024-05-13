# 백준 1713_후보 추천하기
# implementation

# 딕셔너리에 # {학생번호 : [추천수, 게시된 시간]} 형태로 저장
import sys
input = sys.stdin.readline

n = int(input()) # 사진틀 개수(후보 수)
m = int(input()) # 총 추천 수

recommend = list(map(int, input().split())) # 추천받은 학생 번호 리스트

picture = {} # {학생번호 : [추천수, 시간]}
cnt = 0
time = 0
for i in recommend:
    if i in picture:
        picture[i][0] += 1
    else:
        if cnt >= n:
            picture = dict(sorted(picture.items(), key=lambda x: (x[1][0], x[1][1]))) # 추천수 오름차순 정렬 (추천수 같으면)-> 시간 순 오름차순 정렬 
            picture_students = list(picture.keys())
            picture.pop(picture_students[0]) # 이미 추천수, 시간으로 오름차순 정렬 되어있으므로 맨 앞 후보 삭제
        picture[i] = [1, time]
        time += 1
        cnt += 1

result = sorted(list(picture.keys())) # picture 딕셔너리의 학생번호(keys())들을 오름차순 정렬한 리스트 생성

print(*result)          