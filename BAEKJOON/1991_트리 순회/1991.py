# 백준 1991_트리 순회
# 재귀

import sys
input = sys.stdin.readline

n = int(input().strip()) # 노드 개수

# 딕셔너리에 {'루트노드':['왼쪽자식', '오른쪽자식'], ...} 형태로 저장
# {'A' : ['B', 'C']}
tree = {}
for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

# 전위순회(루트 -> 왼 -> 오)
def preorder(v):
    if v != '.': # 자식이 있으면
        print(v, end='')
        preorder(tree[v][0])
        preorder(tree[v][1])

# 중위순회(왼->루트->오)
def inorder(v):
    if v != '.':
        inorder(tree[v][0])
        print(v, end='')
        inorder(tree[v][1])

# 후위순회(왼->오->루트)
def postorder(v):
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end='')

# A가 루트노드
preorder('A')
print()
inorder('A')
print()
postorder('A')