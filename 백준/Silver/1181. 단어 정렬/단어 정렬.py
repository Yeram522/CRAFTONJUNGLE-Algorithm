import heapq
from typing import MutableSequence
from functools import reduce
def heap_sort(a : MutableSequence):
    """힙 정렬"""
    
    def down_heap( a: MutableSequence, left:int, right:int)->None:
        temp = a[left] # 루트
        # left 이외에는 모두 힙 상태라 가정하고 a[left]를 아랫부분의 알맞은 위치로 옮겨 힙 상태를 만든다.
        parent = left
        
        while parent < (right+1) // 2:
            cl = parent * 2 + 1 # 왼쪽 자식
            cr = cl + 1 # 오른쪽 자식
            
            if cr <= right and len(a[cr]) > len(a[cl]):  # 왼, 오 자식 중 큰 값 선택
                child = cr
            elif cr <= right and len(a[cr]) == len(a[cl]): # 길이가 같다면!
                # 사전순으로
                child = cr if a[cr] > a[cl] else cl
           
            else: 
                child = cl
            
            
            if len(temp) > len(a[child]):
                break
            elif len(temp) == len(a[child]) and temp > a[child]: ## 이 조건을 안넣어서 안됨! 주의!!
                break
            
            a[parent] = a[child]
            parent = child
        a[parent] = temp
        
    
    n = len(a)
    
    for i in range((n-1)//2, -1,-1): #a[i]~a[n-1]을 힙으로 만들기
        down_heap(a,i, n-1)
        
        
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i] , a[0] #최댓값인 a[0]와 마지막 원소를 교환
        down_heap(a,0,i-1)  #a[0]~ a[i-1]을 힙으로 만든다.    
        
if __name__ == '__main__':  
    num = int(input())
    
    x = [None] * num
    for i in range(num):
        x[i] = input()
        
    heap_sort(x)
    
    result = reduce(lambda acc, cur: acc if cur in acc else acc+[cur], x, [])
    for i in result:
        print(i)
        
        



        