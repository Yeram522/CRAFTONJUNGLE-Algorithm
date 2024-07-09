# 최대 힙
import sys
from heapq import heappush, heappop
input=sys.stdin.readline # input함수 바꾸기

N = int(input())

max_heap = []
result = list()
for i in range(0,N):
    item = int(input())
    
    
    
    if(item == 0): 
        if len(max_heap) == 0 :
        #print(0)
            result.append(0)
            continue
        #print(heappop(max_heap)[1])
        result.append(heappop(max_heap)[1])
        continue
    
    heappush(max_heap, (-item, item))  # (우선 순위, 값)
    
for r in result:
    print(r)