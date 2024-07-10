import sys
import collections 

input=sys.stdin.readline # input함수 바꾸기

N = int(input())
arr = list(map(int, input().split(' ')))

M = int(input())
targets = list(map(int, input().split(' ')))
# 1. 오름 차순으로 정렬
arr.sort()

# 2. 이분 탐색
def binary_search(t):
    st = 0
    en = len(arr)-1

    while(st<=en):
    # 배열의 중앙 인덱스
        mid = (st + en) // 2
    
        if arr[mid] < t: # 중앙보다 target N이 더 크다면 범위를 오른쪽으로 줄인다.
            st = mid+1
        elif arr[mid] > t:
            en = mid-1 # 범위를 왼쪽으로 줄인다.
        else: # 같다면
            return 1
        
    return 0

for target in targets:
    print(binary_search(target))
        
        