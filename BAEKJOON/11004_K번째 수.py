# 백준 11004_K번째 수
# Sorting

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort() # 오름차순 정렬
print(A[k-1])

'''
# heapq 사용 힙정렬
# 시간 초과

import heapq, sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

def heapsort(arr):
    heap = []
    result = []
    for value in arr:
        heapq.heappush(heap, value)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

result = heapsort(A)
print(result[k-1])

'''

'''
# 힙정렬 구현
# 시간초과

def heapify(arr, n, i):
    largest = i  # 가장 큰 값은 현재 노드로 설정
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    
    # 왼쪽 자식이 부모보다 크다면 인덱스 업데이트
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    
    # 오른쪽 자식이 부모보다 크다면 인덱스 업데이트
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    
    # 최대값이 자식 노드로 이동한 경우 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 변경된 노드에서 재귀적으로 heapify 호출
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # 최대 heap 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 정렬 수행
    for i in range(n - 1, 0, -1):
        # 루트 노드(최대값)와 마지막 노드 교환
        arr[i], arr[0] = arr[0], arr[i]
        # 변경된 heap에서 다시 최대 heap 구성
        heapify(arr, i, 0)


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

heap_sort(A)
print(A[k-1])

'''

