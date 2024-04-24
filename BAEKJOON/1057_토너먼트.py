# 백준 1057_토너먼트
# 완전탐색, 수학

# 풀이 참고
import sys
input = sys.stdin.readline

n, jm, hs = map(int, input().split())

# 번호 매기는 순서 : 처음 번호를 유지하면서 1번부터 매김
# 이겼을 때 다음 라운드의 번호 => n - n//2
# 앞에 진 사람들(절반)을 빼서 자기 번호로 초기화

# 지민, 한수의 다음 라운드에서의 번호가 같을 때 둘이 대결
cnt = 0
while jm != hs:
    jm -= jm // 2 
    hs -= hs // 2
    cnt += 1
    
print(cnt)

# 서로 대결하지 않는 경우는 없다. (언젠가는 대결)
# 왜냐하면, 조건1. 토너먼트 방식 2. 지민 한수는 서로 만나기 전까지 항상 이김
# 따라서 서로 대결하지 않는 경우 -1을 출력하는 부분 구현 X