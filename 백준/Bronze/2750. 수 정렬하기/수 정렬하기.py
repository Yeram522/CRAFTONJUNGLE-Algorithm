#이진 삽입 정렬 알고리즘

from typing import MutableSequence

N = int(input())

x = [None]*N

def binary_insertion_sort(a: MutableSequence)-> None:

    for i in range(1, N):
        key = x[i]
        pl = 0
        pr = i - 1
    
        while True:
            pc = (pl + pr) // 2
        
            if x[pc] == key:
                break
            elif x[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1 #삽입해야할 위치의 인덱스
    
        for j in range(i, pd, -1):
            x[j] = x[j-1]
        x[pd] = key
        
        

    
for n in range(N):
    x[n] = int(input())

binary_insertion_sort(x)

for i in range(N):
    print(x[i])
    
        
        

    
    

    