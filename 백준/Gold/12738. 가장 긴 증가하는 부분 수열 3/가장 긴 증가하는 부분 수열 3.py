import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))
bi = [0 for _ in range(N)]

def binary_search(left, right,key):
    mid = 0
    
    while(left < right):
        mid = int((left+right)/2)
        
        if(bi[mid] < key):
            left = mid + 1
        else:
            right = mid
            
    return right

last_num = 0
seq_count = 1
bi[last_num] = arr[0]

for i in range(1,N):
    if(bi[last_num] < arr[i]):
        last_num += 1
        seq_count += 1
        bi[last_num] = arr[i]
    else:
        idx = binary_search(0, seq_count,arr[i])
        bi[idx] = arr[i]
        
        
print(seq_count)

    
    
        

