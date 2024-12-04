import sys
input = sys.stdin.readline

# N
N = int(input())
lst1 = list(map(int, input().split()))

# M
M = int(input())
lst2 = list(map(int, input().split()))

lst1.sort() # 오른차순 정렬


def binary_search(array, target, start, end):
    if(start > end ): return None # 종료 조건
    
    mid = (start + end) // 2 # 정수로 떨어지도록 나누기
    
    if(array[mid] == target):
        return target
    elif(array[mid] > target): # target이 중간보다 작으면 범위를 왼쪽으로 줄인다.
        return binary_search(array, target, start, mid - 1)
    else: # target이 중간보다 크면 범위를 오른쪽으로 줄인다.
        return binary_search(array, target, mid + 1, end) 
        
result = list()
# lst1에 lst2의 원소가 있는지 체크하고 print 한다.
for elem in lst2:
    res = binary_search(lst1, elem, 0, N-1)
    
    if(res == None):
        result.append(0)
    else:
        result.append(1)
        
print(*result, sep=' ')