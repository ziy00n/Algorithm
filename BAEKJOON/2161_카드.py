# 백준 2161번 카드
# implementation

n = int(input())

cards = [i for i in range(1, n+1)]
result = []

while len(cards) != 1:
    result.append(cards.pop(0)) # 제일 위 카드 버리기
    cards.append(cards.pop(0)) # 그 다음 제일 위 카드를 제일 아래로 옮기기

result.append(cards.pop(0))

print(*result)